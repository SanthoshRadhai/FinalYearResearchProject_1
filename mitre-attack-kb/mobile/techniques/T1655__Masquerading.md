# T1655: Masquerading


**ATT&CK ID:** T1655  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1655  

## Description
Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name, location, or appearance of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1655)

## Sub-techniques
- T1655.001: Match Legitimate Name or Location

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1225: CherryBlos
- S9004: Crocodilus
- S1208: FjordPhantom
- S1185: LightSpy
- S9006: VajraSpy
