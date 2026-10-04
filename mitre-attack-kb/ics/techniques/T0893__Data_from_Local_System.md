# T0893: Data from Local System


**ATT&CK ID:** T0893  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0893  

## Description
Adversaries may target and collect data from local system sources, such as file systems, configuration files, or local databases. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes.

Adversaries may do this using [Command-Line Interface](https://attack.mitre.org/techniques/T0807) or [Scripting](https://attack.mitre.org/techniques/T0853) techniques to interact with the file system to gather information. Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T0802) on the local system.

## Mitigations
- M0803: Data Loss Prevention
- M0917: User Training
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information

## Known Software Using This Technique
- S1000: ACAD/Medre.A
- S0038: Duqu
- S0143: Flame
