# T0873: Project File Infection


**ATT&CK ID:** T0873  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0873  

## Description
Adversaries may attempt to infect project files with malicious code. These project files may consist of objects, program organization units, variables such as tags, documentation, and other configurations needed for PLC programs to function.(Citation: Beckhoff) Using built in functions of the engineering software, adversaries may be able to download an infected program to a PLC in the operating environment enabling further [Execution](https://attack.mitre.org/tactics/TA0104) and [Persistence](https://attack.mitre.org/tactics/TA0110) techniques.(Citation: PLCdev) 

Adversaries may export their own code into project files with conditions to execute at specific intervals.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011) Malicious programs allow adversaries control of all aspects of the process enabled by the PLC. Once the project file is downloaded to a PLC the workstation device may be disconnected with the infected project file still executing.(Citation: PLCdev)

## Sub-techniques
- T0873.001: Siemens Project File Format

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0947: Audit
