# T1204: User Execution


**ATT&CK ID:** T1204  
**Domain:** Mitre Attack  
**Tactic(s):** Execution  
**Platforms:** Linux, Windows, macOS, IaaS, Containers  
**Reference:** https://attack.mitre.org/techniques/T1204  

## Description
An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [Phishing](https://attack.mitre.org/techniques/T1566).

While [User Execution](https://attack.mitre.org/techniques/T1204) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

Adversaries may also deceive users into performing actions such as:

* Enabling [Remote Access Tools](https://attack.mitre.org/techniques/T1219), allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)s(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)
* Downloading and executing malware for [User Execution](https://attack.mitre.org/techniques/T1204)
* Coerceing users to copy, paste, and execute malicious code manually(Citation: Reliaquest-execution)(Citation: proofpoint-selfpwn)

For example, tech support scams can be facilitated through [Phishing](https://attack.mitre.org/techniques/T1566), vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [Remote Access Tools](https://attack.mitre.org/techniques/T1219).(Citation: Telephone Attack Delivery)

## Sub-techniques
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1204.003: Malicious Image
- T1204.004: Malicious Copy and Paste
- T1204.005: Malicious Library

## Mitigations
- M1017: User Training
- M1021: Restrict Web-Based Content
- M1031: Network Intrusion Prevention
- M1033: Limit Software Installation
- M1038: Execution Prevention
- M1040: Behavior Prevention on Endpoint

## Known Threat Groups Using This Technique
- G1004: LAPSUS$
- G1015: Scattered Spider

## Known Software Using This Technique
- S1213: Lumma Stealer
- S1130: Raspberry Robin
