# T0861: Point & Tag Identification


**ATT&CK ID:** T0861  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0861  

## Description
Adversaries may collect point and tag values to gain a more comprehensive understanding of the process environment. Points may be values such as inputs, memory locations, outputs or other process specific variables. (Citation: Dennis L. Sloatman September 2016) Tags are the identifiers given to points for operator convenience. 

Collecting such tags provides valuable context to environmental points and enables an adversary to map inputs, outputs, and other values to their control processes. Understanding the points being collected may inform an adversary on which processes and values to keep track of over the course of an operation.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER
