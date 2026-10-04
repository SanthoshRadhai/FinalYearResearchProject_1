# T1114: Email Collection


**ATT&CK ID:** T1114  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Windows, macOS, Linux, Office Suite  
**Reference:** https://attack.mitre.org/techniques/T1114  

## Description
Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses.(Citation: TrustedSec OOB Communications)(Citation: CISA AA20-352A 2021) Adversaries can collect or forward email from mail servers or clients.

## Sub-techniques
- T1114.001: Local Email Collection
- T1114.002: Remote Email Collection
- T1114.003: Email Forwarding Rule

## Mitigations
- M1032: Multi-factor Authentication
- M1041: Encrypt Sensitive Information
- M1047: Audit
- M1060: Out-of-Band Communications Channel

## Known Threat Groups Using This Technique
- G1003: Ember Bear
- G0059: Magic Hound
- G1015: Scattered Spider
- G0122: Silent Librarian

## Known Software Using This Technique
- S0367: Emotet
- S1201: TRANSLATEXT
