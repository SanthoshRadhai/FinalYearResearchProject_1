# T0826: Loss of Availability


**ATT&CK ID:** T0826  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0826  

## Description
Adversaries may attempt to disrupt essential components or systems to prevent owner and operator from delivering products or services. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

Adversaries may leverage malware to delete or encrypt critical data on HMIs, workstations, or databases.

In the 2021 Colonial Pipeline ransomware incident, pipeline operations were temporally halted on May 7th and were not fully restarted until May 12th. (Citation: Colonial Pipeline Company May 2021)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0608: Conficker
