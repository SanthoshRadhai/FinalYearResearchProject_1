# T1417: Input Capture


**ATT&CK ID:** T1417  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1417  

## Description
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal device usage, users often provide credentials to various locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Keylogging](https://attack.mitre.org/techniques/T1417/001)) or rely on deceiving the user into providing input into what they believe to be a genuine application prompt (e.g. [GUI Input Capture](https://attack.mitre.org/techniques/T1417/002)).

## Sub-techniques
- T1417.001: Keylogging
- T1417.002: GUI Input Capture

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1225: CherryBlos
- S1231: GodFather
- S1126: Phenakite
