# T1548: Abuse Elevation Control Mechanism


**ATT&CK ID:** T1548  
**Domain:** Mitre Attack  
**Tactic(s):** Privilege Escalation  
**Platforms:** Linux, macOS, Windows, IaaS, Office Suite, Identity Provider  
**Reference:** https://attack.mitre.org/techniques/T1548  

## Description
Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk.(Citation: TechNet How UAC Works)(Citation: sudo man page 2018) An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.(Citation: OSX Keydnap malware)(Citation: Fortinet Fareit)

## Sub-techniques
- T1548.001: Setuid and Setgid
- T1548.002: Bypass User Account Control
- T1548.003: Sudo and Sudo Caching
- T1548.004: Elevated Execution with Prompt
- T1548.005: Temporary Elevated Cloud Access
- T1548.006: TCC Manipulation

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1026: Privileged Account Management
- M1028: Operating System Configuration
- M1038: Execution Prevention
- M1047: Audit
- M1051: Update Software
- M1052: User Account Control

## Known Threat Groups Using This Technique
- G1048: UNC3886

## Known Software Using This Technique
- S1130: Raspberry Robin
