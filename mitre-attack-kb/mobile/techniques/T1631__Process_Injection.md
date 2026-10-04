# T1631: Process Injection


**ATT&CK ID:** T1631  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Privilege Escalation  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1631  

## Description
Adversaries may inject code into processes in order to evade process-based defenses or even elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

Both Android and iOS have no legitimate way to achieve process injection. The only way this is possible is by abusing existing root access or exploiting a vulnerability.

## Sub-techniques
- T1631.001: Ptrace System Calls

## Known Software Using This Technique
- S1208: FjordPhantom
- S1185: LightSpy
