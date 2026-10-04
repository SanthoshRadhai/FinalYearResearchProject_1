"""Session index -- a plain table (separate from LangGraph's own checkpoint
tables) that exists only so the Gradio sidebar has something browsable to
list: titles, timestamps, and each session's last-used model settings. The
actual conversation history itself lives in LangGraph's checkpointer, keyed
by the same id used here as `session_id` (== the graph's `thread_id`).
"""

import json
import sqlite3
import time
import uuid
from pathlib import Path

from checkpointer import DB_PATH
from llm import DEFAULT_SETTINGS


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.row_factory = sqlite3.Row
    return conn


def init_sessions_table() -> None:
    conn = _connect()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at REAL NOT NULL,
            last_used REAL NOT NULL,
            settings_json TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def create_session(title: str = "New chat") -> str:
    session_id = str(uuid.uuid4())
    now = time.time()
    conn = _connect()
    conn.execute(
        "INSERT INTO sessions (session_id, title, created_at, last_used, settings_json) "
        "VALUES (?, ?, ?, ?, ?)",
        (session_id, title, now, now, json.dumps(DEFAULT_SETTINGS)),
    )
    conn.commit()
    conn.close()
    return session_id


def list_sessions() -> list[dict]:
    conn = _connect()
    rows = conn.execute(
        "SELECT session_id, title, created_at, last_used, settings_json "
        "FROM sessions ORDER BY last_used DESC"
    ).fetchall()
    conn.close()
    return [
        {
            "session_id": r["session_id"],
            "title": r["title"],
            "created_at": r["created_at"],
            "last_used": r["last_used"],
            "settings": json.loads(r["settings_json"]),
        }
        for r in rows
    ]


def get_session(session_id: str) -> dict | None:
    conn = _connect()
    row = conn.execute(
        "SELECT session_id, title, created_at, last_used, settings_json "
        "FROM sessions WHERE session_id = ?",
        (session_id,),
    ).fetchone()
    conn.close()
    if row is None:
        return None
    return {
        "session_id": row["session_id"],
        "title": row["title"],
        "created_at": row["created_at"],
        "last_used": row["last_used"],
        "settings": json.loads(row["settings_json"]),
    }


def touch_session(session_id: str) -> None:
    conn = _connect()
    conn.execute("UPDATE sessions SET last_used = ? WHERE session_id = ?", (time.time(), session_id))
    conn.commit()
    conn.close()


def rename_session(session_id: str, title: str) -> None:
    conn = _connect()
    conn.execute("UPDATE sessions SET title = ? WHERE session_id = ?", (title, session_id))
    conn.commit()
    conn.close()


def update_session_settings(session_id: str, settings: dict) -> None:
    conn = _connect()
    conn.execute(
        "UPDATE sessions SET settings_json = ? WHERE session_id = ?",
        (json.dumps(settings), session_id),
    )
    conn.commit()
    conn.close()


def delete_session(session_id: str) -> None:
    conn = _connect()
    conn.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
    # LangGraph's own checkpoint tables, keyed by thread_id == session_id.
    conn.execute("DELETE FROM checkpoints WHERE thread_id = ?", (session_id,))
    conn.execute("DELETE FROM writes WHERE thread_id = ?", (session_id,))
    conn.commit()
    conn.close()
