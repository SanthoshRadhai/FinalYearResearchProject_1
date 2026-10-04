# T1552: Unsecured Credentials


**ATT&CK ID:** T1552  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** Windows, SaaS, IaaS, Linux, macOS, Containers, Network Devices, Office Suite, Identity Provider  
**Reference:** https://attack.mitre.org/techniques/T1552  

## Description
Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Shell History](https://attack.mitre.org/techniques/T1552/003)), operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)),  or other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).(Citation: Brining MimiKatz to Unix)

## Sub-techniques
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1552.003: Shell History
- T1552.004: Private Keys
- T1552.005: Cloud Instance Metadata API
- T1552.006: Group Policy Preferences
- T1552.007: Container API
- T1552.008: Chat Messages

## Mitigations
- M1015: Active Directory Configuration
- M1017: User Training
- M1022: Restrict File and Directory Permissions
- M1026: Privileged Account Management
- M1027: Password Policies
- M1028: Operating System Configuration
- M1035: Limit Access to Resource Over Network
- M1037: Filter Network Traffic
- M1041: Encrypt Sensitive Information
- M1047: Audit
- M1051: Update Software

## Known Threat Groups Using This Technique
- G1017: Volt Typhoon

## Known Software Using This Technique
- S0373: Astaroth
- S1111: DarkGate
- S1131: NPPSPY
- S1091: Pacu
