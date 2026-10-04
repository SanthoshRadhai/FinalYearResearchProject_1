# T1661: Application Versioning


**ATT&CK ID:** T1661  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access, Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1661  

## Description
An adversary may push an update to a previously benign application to add malicious code. This can be accomplished by pushing an initially benign, functional application to a trusted application store, such as the Google Play Store or the Apple App Store. This allows the adversary to establish a trusted userbase that may grant permissions to the application prior to the introduction of malicious code. Then, an application update could be pushed to introduce malicious code.(Citation: android_app_breaking_bad)

This technique could also be accomplished by compromising a developer’s account. This would allow an adversary to take advantage of an existing userbase without having to establish the userbase themselves.

## Mitigations
- M1006: Use Recent OS Version
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1055: SharkBot
