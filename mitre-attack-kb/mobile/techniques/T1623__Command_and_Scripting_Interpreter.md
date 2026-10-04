# T1623: Command and Scripting Interpreter


**ATT&CK ID:** T1623  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Execution  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1623  

## Description
Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, Android is a UNIX-like OS and includes a basic [Unix Shell](https://attack.mitre.org/techniques/T1623/001) that can be accessed via the Android Debug Bridge (ADB) or Java’s `Runtime` package.

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [Initial Access](https://attack.mitre.org/tactics/TA0027) payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells.

## Sub-techniques
- T1623.001: Unix Shell

## Mitigations
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1185: LightSpy
- S1056: TianySpy
