# T1098: Account Manipulation


**ATT&CK ID:** T1098  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence, Privilege Escalation  
**Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1098  

## Description
Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## Sub-techniques
- T1098.001: Additional Cloud Credentials
- T1098.002: Additional Email Delegate Permissions
- T1098.003: Additional Cloud Roles
- T1098.004: SSH Authorized Keys
- T1098.005: Device Registration
- T1098.006: Additional Container Cluster Roles
- T1098.007: Additional Local or Domain Groups

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1026: Privileged Account Management
- M1028: Operating System Configuration
- M1030: Network Segmentation
- M1032: Multi-factor Authentication
- M1042: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0125: HAFNIUM
- G0032: Lazarus Group
- G1015: Scattered Spider
- G1056: TeamPCP
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S0274: Calisto
- S0002: Mimikatz
- S9008: Shai-Hulud
