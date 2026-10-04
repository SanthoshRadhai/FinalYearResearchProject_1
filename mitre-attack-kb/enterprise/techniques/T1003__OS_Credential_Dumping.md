# T1003: OS Credential Dumping


**ATT&CK ID:** T1003  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1003  

## Description
Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining MimiKatz to Unix) Credentials can then be used to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and access restricted information.

Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.

## Sub-techniques
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1003.006: DCSync
- T1003.007: Proc Filesystem
- T1003.008: /etc/passwd and /etc/shadow

## Mitigations
- M1015: Active Directory Configuration
- M1017: User Training
- M1025: Privileged Process Integrity
- M1026: Privileged Account Management
- M1027: Password Policies
- M1028: Operating System Configuration
- M1040: Behavior Prevention on Endpoint
- M1041: Encrypt Sensitive Information
- M1043: Credential Access Protection

## Known Threat Groups Using This Technique
- G0007: APT28
- G0050: APT32
- G0087: APT39
- G0001: Axiom
- G1043: BlackByte
- G1003: Ember Bear
- G0065: Leviathan
- G0129: Mustang Panda
- G0033: Poseidon Group
- G0054: Sowbug
- G1053: Storm-0501
- G0039: Suckfly
- G0131: Tonto Team

## Known Software Using This Technique
- S0030: Carbanak
- S0232: HOMEFRY
- S1146: MgBot
- S0052: OnionDuke
- S0048: PinchDuke
- S0379: Revenge RAT
- S0094: Trojan.Karagany
