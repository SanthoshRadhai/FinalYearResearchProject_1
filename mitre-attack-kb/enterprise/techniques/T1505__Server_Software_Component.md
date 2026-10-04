# T1505: Server Software Component


**ATT&CK ID:** T1505  
**Domain:** Mitre Attack  
**Tactic(s):** Persistence  
**Platforms:** Windows, Linux, macOS, Network Devices, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1505  

## Description
Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications.(Citation: volexity_0day_sophos_FW)

## Sub-techniques
- T1505.001: SQL Stored Procedures
- T1505.002: Transport Agent
- T1505.003: Web Shell
- T1505.004: IIS Components
- T1505.005: Terminal Services DLL
- T1505.006: vSphere Installation Bundles

## Mitigations
- M1018: User Account Management
- M1024: Restrict Registry Permissions
- M1026: Privileged Account Management
- M1042: Disable or Remove Feature or Program
- M1045: Code Signing
- M1046: Boot Integrity
- M1047: Audit
