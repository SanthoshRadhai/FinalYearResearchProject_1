# T0832: Manipulation of View


**ATT&CK ID:** T0832  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0832  

## Description
Adversaries may attempt to manipulate the information reported back to operators or controllers. This manipulation may be short term or sustained. During this time the process itself could be in a much different state than what is reported. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

Operators may be fooled into doing something that is harmful to the system in a loss of view situation. With a manipulated view into the systems, operators may issue inappropriate control sequences that introduce faults or catastrophic failures into the system. Business analysis systems can also be provided with inaccurate data leading to bad management decisions.

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
- S0603: Stuxnet
