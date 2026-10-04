# T1624: Event Triggered Execution


**ATT&CK ID:** T1624  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1624  

## Description
Adversaries may establish persistence using system mechanisms that trigger execution based on specific events. Mobile operating systems have means to subscribe to events such as receiving an SMS message, device boot completion, or other device activities. 

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via automatically and repeatedly executing malicious code. After gaining access to a victim’s system, adversaries may create or modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.

## Sub-techniques
- T1624.001: Broadcast Receivers

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1079: BOULDSPY
- S1231: GodFather
