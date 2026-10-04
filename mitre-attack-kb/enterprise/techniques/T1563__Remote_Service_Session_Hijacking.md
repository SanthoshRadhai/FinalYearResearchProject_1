# T1563: Remote Service Session Hijacking


**ATT&CK ID:** T1563  
**Domain:** Mitre Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1563  

## Description
Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563) differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: RDP Hijacking Medium)(Citation: Breach Post-mortem SSH Hijack)

## Sub-techniques
- T1563.001: SSH Hijacking
- T1563.002: RDP Hijacking

## Mitigations
- M1018: User Account Management
- M1026: Privileged Account Management
- M1027: Password Policies
- M1030: Network Segmentation
- M1042: Disable or Remove Feature or Program
