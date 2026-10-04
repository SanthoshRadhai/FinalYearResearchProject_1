# T0811: Data from Information Repositories


**ATT&CK ID:** T0811  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0811  

## Description
Adversaries may target and collect data from information repositories. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes. Examples of information repositories include reference databases in the process environment, as well as databases in the corporate network that might contain information about the ICS.(Citation: Cybersecurity & Infrastructure Security Agency March 2018)

Information collected from these systems may provide the adversary with a better understanding of the operational environment, vendors used, processes, or procedures of the ICS.

In a campaign between 2011 and 2013 against ONG organizations, Chinese state-sponsored actors searched document repositories for specific information such as, system manuals, remote terminal unit (RTU) sites, personnel lists, documents that included the string SCAD*, user credentials, and remote dial-up access information. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0918: User Account Management
- M0922: Restrict File and Directory Permissions
- M0926: Privileged Account Management
- M0941: Encrypt Sensitive Information
- M0947: Audit

## Known Software Using This Technique
- S0038: Duqu
