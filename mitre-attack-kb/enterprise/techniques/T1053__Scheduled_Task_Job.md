# T1053: Scheduled Task/Job


**ATT&CK ID:** T1053  
**Domain:** Mitre Attack  
**Tactic(s):** Execution, Persistence, Privilege Escalation  
**Platforms:** Containers, ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1053  

## Description
Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system.(Citation: TechNet Task Scheduler Security)

Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges). Similar to [System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218), adversaries have also abused task scheduling to potentially mask one-time execution under a trusted system process.(Citation: ProofPoint Serpent)

## Sub-techniques
- T1053.002: At
- T1053.003: Cron
- T1053.004: Launchd
- T1053.005: Scheduled Task
- T1053.006: Systemd Timers
- T1053.007: Container Orchestration Job

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1026: Privileged Account Management
- M1028: Operating System Configuration
- M1047: Audit

## Known Software Using This Technique
- S0447: Lokibot
