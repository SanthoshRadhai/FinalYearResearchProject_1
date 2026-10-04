# T1556: Modify Authentication Process


**ATT&CK ID:** T1556  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment, Persistence, Credential Access  
**Platforms:** IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1556  

## Description
Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.

## Sub-techniques
- T1556.001: Domain Controller Authentication
- T1556.002: Password Filter DLL
- T1556.003: Pluggable Authentication Modules
- T1556.004: Network Device Authentication
- T1556.005: Reversible Encryption
- T1556.006: Multi-Factor Authentication
- T1556.007: Hybrid Identity
- T1556.008: Network Provider DLL
- T1556.009: Conditional Access Policies

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1024: Restrict Registry Permissions
- M1025: Privileged Process Integrity
- M1026: Privileged Account Management
- M1027: Password Policies
- M1028: Operating System Configuration
- M1032: Multi-factor Authentication
- M1047: Audit

## Known Threat Groups Using This Technique
- G1016: FIN13

## Known Software Using This Technique
- S9013: DRYHOOK
- S0377: Ebury
- S0487: Kessel
- S0692: SILENTTRINITY
