# T1625: Hijack Execution Flow


**ATT&CK ID:** T1625  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1625  

## Description
Adversaries may execute their own malicious payloads by hijacking the way operating systems run applications. Hijacking execution flow can be for the purposes of persistence since this hijacked execution may reoccur over time. 

There are many ways an adversary may hijack the flow of execution. A primary way is by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs or resources, such as file directories, could also be poisoned to include malicious payloads.

## Sub-techniques
- T1625.001: System Runtime API Hijacking

## Mitigations
- M1002: Attestation
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0311: YiSpecter
