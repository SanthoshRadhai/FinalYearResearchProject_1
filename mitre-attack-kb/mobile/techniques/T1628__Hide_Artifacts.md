# T1628: Hide Artifacts


**ATT&CK ID:** T1628  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1628  

## Description
Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Mobile operating systems have features and developer APIs to hide various artifacts, such as an application’s launcher icon. These APIs have legitimate usages, such as hiding an icon to avoid application drawer clutter when an application does not have a usable interface. Adversaries may abuse these features and APIs to hide artifacts from the user to evade detection.

## Sub-techniques
- T1628.001: Suppress Application Icon
- T1628.002: User Evasion
- T1628.003: Conceal Multimedia Files
