# T1629: Impair Defenses


**ATT&CK ID:** T1629  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1629  

## Description
Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive mechanisms. This not only involves impairing preventative defenses, such as anti-virus, but also detection capabilities that defenders can use to audit activity and identify malicious behavior. This may span both native defenses as well as supplemental capabilities installed by users or mobile endpoint administrators.

## Sub-techniques
- T1629.001: Prevent Application Removal
- T1629.002: Device Lockout
- T1629.003: Disable or Modify Tools

## Mitigations
- M1001: Security Updates
- M1004: System Partition Integrity
- M1010: Deploy Compromised Device Detection Method
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1225: CherryBlos
- S1231: GodFather
