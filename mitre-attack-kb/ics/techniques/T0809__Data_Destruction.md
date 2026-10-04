# T0809: Data Destruction


**ATT&CK ID:** T0809  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0809  

## Description
Adversaries may perform data destruction over the course of an operation. The adversary may drop or create malware, tools, or other non-native files on a target system to accomplish this, potentially leaving behind traces of malicious activities. Such non-native files and other data may be removed over the course of an intrusion to maintain a small footprint or as a standard part of the post-intrusion cleanup process. (Citation: Enterprise ATT&CK January 2018)

Data destruction may also be used to render operator interfaces unable to respond and to disrupt response functions from occurring as expected. An adversary may also destroy data backups that are vital to recovery after an incident.

Standard file deletion commands are available on most operating system and device interfaces to perform cleanup, but adversaries may use other tools as well. Two examples are Windows Sysinternals SDelete and Active@ Killdisk.

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0926: Privileged Account Management
- M0953: Data Backup

## Known Software Using This Technique
- S1157: Fuxnet
- S1045: INCONTROLLER
- S0604: Industroyer
- S0607: KillDisk
