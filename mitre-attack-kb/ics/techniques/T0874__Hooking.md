# T0874: Hooking


**ATT&CK ID:** T0874  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution, Privilege Escalation  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0874  

## Description
Adversaries may hook into application programming interface (API) functions used by processes to redirect calls for execution and privilege escalation means. Windows processes often leverage these API functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. (Citation: Enterprise ATT&CK)

One type of hooking seen in ICS involves redirecting calls to these functions via import address table (IAT) hooking. IAT hooking uses modifications to a process IAT, where pointers to imported API functions are stored. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Mitigations
- M0944: Restrict Library Loading
- M0947: Audit

## Known Software Using This Technique
- S0603: Stuxnet
- S1009: Triton
