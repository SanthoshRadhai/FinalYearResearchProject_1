# T0878: Alarm Suppression


**ATT&CK ID:** T0878  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0878  

## Description
Adversaries may target protection function alarms to prevent them from notifying operators of critical conditions. Alarm messages may be a part of an overall reporting system and of particular interest for adversaries. Disruption of the alarm system does not imply the disruption of the reporting system as a whole.

A Secura presentation on targeting OT notes a dual fold goal for adversaries attempting alarm suppression: prevent outgoing alarms from being raised and prevent incoming alarms from being responded to. (Citation: Jos Wetzels, Marina Krotofil 2019) The method of suppression may greatly depend on the type of alarm in question:  

* An alarm raised by a protocol message 
* An alarm signaled with I/O 
* An alarm bit set in a flag (and read) 

In ICS environments, the adversary may have to suppress or contend with multiple alarms and/or alarm propagation to achieve a specific goal to evade detection or prevent intended responses from occurring. (Citation: Jos Wetzels, Marina Krotofil 2019)  Methods of suppression may involve tampering or altering device displays and logs, modifying in memory code to fixed values, or even tampering with assembly level instruction code.

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0814: Static Network Configuration
- M0930: Network Segmentation
