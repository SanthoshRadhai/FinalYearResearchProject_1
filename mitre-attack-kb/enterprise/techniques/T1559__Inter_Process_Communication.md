# T1559: Inter-Process Communication


**ATT&CK ID:** T1559  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1559  

## Description
Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) or [Component Object Model](https://attack.mitre.org/techniques/T1559/001). Linux environments support several different IPC mechanisms, two of which being sockets and pipes.(Citation: Linux IPC) Higher level execution mediums, such as those of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)s, may also leverage underlying IPC mechanisms. Adversaries may also use [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) to facilitate remote IPC execution.(Citation: Fireeye Hunting COM June 2019)

## Sub-techniques
- T1559.001: Component Object Model
- T1559.002: Dynamic Data Exchange
- T1559.003: XPC Services

## Mitigations
- M1013: Application Developer Guidance
- M1026: Privileged Account Management
- M1040: Behavior Prevention on Endpoint
- M1042: Disable or Remove Feature or Program
- M1048: Application Isolation and Sandboxing
- M1054: Software Configuration

## Known Software Using This Technique
- S0687: Cyclops Blink
- S1229: Havoc
- S0537: HyperStack
- S1141: LunarWeb
- S1244: Medusa Ransomware
- S9043: Mini Shai-Hulud
- S1100: Ninja
- S1172: OilBooster
- S1123: PITSTOP
- S1150: ROADSWEEP
- S1130: Raspberry Robin
- S1078: RotaJakiro
- S9024: SPAWNCHIMERA
- S1200: StealBit
- S1239: TONESHELL
- S0022: Uroburos
