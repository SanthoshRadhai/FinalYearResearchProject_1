# TA0104: Execution

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0104  

## Description
The adversary is trying to run code or manipulate system functions, parameters, and data in an unauthorized way.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system, device, or other asset. This execution may also rely on unknowing end users or the manipulation of device operating modes to run. Adversaries may infect remote targets with programmed executables or malicious project files that operate according to specified behavior and may alter expected device behavior in subtle ways. Commands for execution may also be issued from command-line interfaces, APIs, GUIs, or other available interfaces. Techniques that run malicious code may also be paired with techniques from other tactics, particularly to aid network [Discovery](https://attack.mitre.org/tactics/TA0102) and [Collection](https://attack.mitre.org/tactics/TA0100), impact operations, and inhibit response functions.

## Techniques in This Tactic
- T0807: Command-Line Interface
- T0821: Modify Controller Tasking
- T0823: Graphical User Interface
- T0834: Native API
- T0853: Scripting
- T0858: Change Operating Mode
- T0863: User Execution
- T0871: Execution through API
- T0874: Hooking
- T0895: Autorun Image
