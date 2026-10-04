# T0815: Denial of View


**ATT&CK ID:** T0815  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0815  

## Description
Adversaries may cause a denial of view in attempt to disrupt and prevent operator oversight on the status of an ICS environment. This may manifest itself as a temporary communication failure between a device and its control source, where the interface recovers and becomes available once the interference ceases. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

An adversary may attempt to deny operator visibility by preventing them from receiving status and reporting messages. Denying this view may temporarily block and prevent operators from noticing a change in state or anomalous behavior. The environment's data and processes may still be operational, but functioning in an unintended or adversarial manner.

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
