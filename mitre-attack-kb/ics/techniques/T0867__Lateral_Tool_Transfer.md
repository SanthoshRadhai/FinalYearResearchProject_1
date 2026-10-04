# T0867: Lateral Tool Transfer


**ATT&CK ID:** T0867  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0867  

## Description
Adversaries may transfer tools or other files from one system to another to stage adversary tools or other files over the course of an operation. (Citation: Enterprise ATT&CK) Copying of files may also be performed laterally between internal victim systems to support Lateral Movement with remote Execution using inherent file sharing protocols such as file sharing over SMB to connected network shares. (Citation: Enterprise ATT&CK)

In control systems environments, malware may use SMB and other file sharing protocols to move laterally through industrial networks.

## Mitigations
- M0931: Network Intrusion Prevention

## Known Software Using This Technique
- S0606: Bad Rabbit
- S1045: INCONTROLLER
- S0368: NotPetya
- S0603: Stuxnet
- S0366: WannaCry
