# T0813: Denial of Control


**ATT&CK ID:** T0813  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0813  

## Description
Adversaries may cause a denial of control to temporarily prevent operators and engineers from interacting with process controls. An adversary may attempt to deny process control access to cause a temporary loss of communication with the control device or to prevent operator adjustment of process controls. An affected process may still be operating during the period of control loss, but not necessarily in a desired state. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

In the 2017 Dallas Siren incident operators were unable to disable the false alarms from the Office of Emergency Management headquarters. (Citation: Mark Loveless April 2017)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
