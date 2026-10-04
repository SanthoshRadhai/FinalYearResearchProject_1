# T1059: Command and Scripting Interpreter


**ATT&CK ID:** T1059  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1059  

## Description
Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [Unix Shell](https://attack.mitre.org/techniques/T1059/004) while Windows installations include the [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

There are also cross-platform interpreters such as [Python](https://attack.mitre.org/techniques/T1059/006), as well as those commonly associated with client applications such as [JavaScript](https://attack.mitre.org/techniques/T1059/007) and [Visual Basic](https://attack.mitre.org/techniques/T1059/005).

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [Initial Access](https://attack.mitre.org/tactics/TA0001) payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various [Remote Services](https://attack.mitre.org/techniques/T1021) in order to achieve remote Execution.(Citation: Powershell Remote Commands)(Citation: Cisco IOS Software Integrity Assurance - Command History)(Citation: Remote Shell Execution in Python)

## Sub-techniques
- T1059.001: PowerShell
- T1059.002: AppleScript
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1059.008: Network Device CLI
- T1059.009: Cloud API
- T1059.010: AutoHotKey & AutoIT
- T1059.011: Lua
- T1059.012: Hypervisor CLI
- T1059.013: Container CLI/API

## Mitigations
- M1021: Restrict Web-Based Content
- M1026: Privileged Account Management
- M1033: Limit Software Installation
- M1038: Execution Prevention
- M1040: Behavior Prevention on Endpoint
- M1042: Disable or Remove Feature or Program
- M1045: Code Signing
- M1047: Audit
- M1049: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G0073: APT19
- G0050: APT32
- G0067: APT37
- G0087: APT39
- G0035: Dragonfly
- G0053: FIN5
- G0037: FIN6
- G0046: FIN7
- G0117: Fox Kitten
- G0004: Ke3chang
- G0129: Mustang Panda
- G0049: OilRig
- G1031: Saint Bear
- G0038: Stealth Falcon
- G0107: Whitefly
- G0124: Windigo
- G1035: Winter Vivern

## Known Software Using This Technique
- S0234: Bandook
- S0486: Bonadan
- S0023: CHOPSTICK
- S0334: DarkComet
- S0695: Donut
- S0363: Empire
- S0618: FIVEHANDS
- S0460: Get2
- S0434: Imminent Monitor
- S0487: Kessel
- S0167: Matryoshka
- S9032: MuddyViper
- S1192: NICECURL
- S0598: P.A.S. Webshell
- S1130: Raspberry Robin
- S1110: SLIGHTPULSE
- S0374: SpeakUp
- S1227: StarProxy
- S1154: VersaMem
- S0219: WINERACK
- S1151: ZeroCleare
- S0330: Zeus Panda
- S0032: gh0st RAT
