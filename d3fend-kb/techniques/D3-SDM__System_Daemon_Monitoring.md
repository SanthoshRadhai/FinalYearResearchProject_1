# D3-SDM: System Daemon Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-SDM/  

## Definition
Tracking changes to the state or configuration of critical system level processes.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - Method using kernel mode assistance for the detection and removal of threats which are actively preventing detection and removal from a running system - Symantec Corporation
- **kb-reference:** Reference - CAR-2016-04-003: User Activity from Stopping Windows Defensive Services - MITRE
- **monitors:** Operating System Process

## Knowledge Base Article
## How it works
Attackers may manipulate system settings or services to disable system logging or monitoring of security tools and events. Firewall and antivirus services are popular targets for attackers. Disabling system logs will also allow an attacker's actions to go unnoticed. Analysis of logs, registries, and process monitoring help defenders locate signs of tampering. Two possible approaches are to monitor hardened system services or to monitor registry updates for modifications to security settings.
