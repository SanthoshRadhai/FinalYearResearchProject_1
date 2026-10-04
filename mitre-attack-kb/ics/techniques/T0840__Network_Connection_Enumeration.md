# T0840: Network Connection Enumeration


**ATT&CK ID:** T0840  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0840  

## Description
Adversaries may perform network connection enumeration to discover information about device communication patterns. If an adversary can inspect the state of a network connection with tools, such as Netstat(Citation: Netstat), in conjunction with [System Firmware](https://attack.mitre.org/techniques/T0857), then they can determine the role of certain devices on the network  (Citation: MITRE). The adversary can also use [Network Sniffing](https://attack.mitre.org/techniques/T0842) to watch network traffic for details about the source, destination, protocol, and content.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Software Using This Technique
- S0605: EKANS
- S0604: Industroyer
