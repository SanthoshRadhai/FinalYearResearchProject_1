# TA0008: Lateral Movement

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0008  

## Description
The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target, then pivoting through multiple systems and accounts to gain access to it. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier.

## Techniques in This Tactic
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.003: Distributed Component Object Model
- T1021.004: SSH
- T1021.005: VNC
- T1021.006: Windows Remote Management
- T1021.007: Cloud Services
- T1021.008: Direct Cloud VM Connections
- T1072: Software Deployment Tools
- T1080: Taint Shared Content
- T1091: Replication Through Removable Media
- T1210: Exploitation of Remote Services
- T1534: Internal Spearphishing
- T1550: Use Alternate Authentication Material
- T1550.001: Application Access Token
- T1550.002: Pass the Hash
- T1550.003: Pass the Ticket
- T1550.004: Web Session Cookie
- T1563: Remote Service Session Hijacking
- T1563.001: SSH Hijacking
- T1563.002: RDP Hijacking
- T1570: Lateral Tool Transfer
