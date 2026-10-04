# T0829: Loss of View


**ATT&CK ID:** T0829  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0829  

## Description
Adversaries may cause a sustained or permanent loss of view where the ICS equipment will require local, hands-on operator intervention; for instance, a restart or manual operation. By causing a sustained reporting or visibility loss, the adversary can effectively hide the present state of operations. This loss of view can occur without affecting the physical processes themselves. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S1157: Fuxnet
- S0604: Industroyer
- S0607: KillDisk
- S0372: LockerGoga
