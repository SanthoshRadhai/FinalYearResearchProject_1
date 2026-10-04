from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from phoenix.otel import register

register(project_name="redblue-graph", auto_instrument=True)

llm = ChatOpenAI(base_url="http://127.0.0.1:5500/v1", api_key="none", model="gpt-oss-20b")

class State(TypedDict):
    target: str
    attack: str
    defense: str

def red(state):
    return {"attack": llm.invoke(f"As a red-team agent, suggest one attack on: {state['target']}. One sentence.").content}

def blue(state):
    return {"defense": llm.invoke(f"As a blue-team agent, suggest one defense against: {state['attack']}. One sentence.").content}

g = StateGraph(State)
g.add_node("red", red)
g.add_node("blue", blue)
g.add_edge(START, "red")
g.add_edge("red", "blue")
g.add_edge("blue", END)
app = g.compile()

print(app.get_graph().draw_mermaid())   # the design graph, as Mermaid text
print(app.invoke({"target": "a login page"}))
