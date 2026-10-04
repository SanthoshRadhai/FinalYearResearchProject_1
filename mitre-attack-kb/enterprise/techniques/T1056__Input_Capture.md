# T1056: Input Capture


**ATT&CK ID:** T1056  
**Domain:** Mitre Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1056  

## Description
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004)) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [Web Portal Capture](https://attack.mitre.org/techniques/T1056/003)).

## Sub-techniques
- T1056.001: Keylogging
- T1056.002: GUI Input Capture
- T1056.003: Web Portal Capture
- T1056.004: Credential API Hooking

## Known Threat Groups Using This Technique
- G0087: APT39
- G1044: APT42
- G1046: Storm-1811

## Known Software Using This Technique
- S0631: Chaes
- S0381: FlawedAmmyy
- S1245: InvisibleFerret
- S0641: Kobalos
- S1060: Mafalda
- S1131: NPPSPY
- S1059: metaMain
