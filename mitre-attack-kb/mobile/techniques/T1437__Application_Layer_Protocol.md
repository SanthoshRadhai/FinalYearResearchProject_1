# T1437: Application Layer Protocol


**ATT&CK ID:** T1437  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1437  

## Description
Adversaries may communicate using application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the mobile device, and often the results of those commands, will be embedded within the protocol traffic between the mobile device and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, or DNS.

## Sub-techniques
- T1437.001: Web Protocols

## Known Software Using This Technique
- S1083: Chameleon
- S1243: DCHSpy
- S0550: DoubleAgent
- S1054: Drinik
