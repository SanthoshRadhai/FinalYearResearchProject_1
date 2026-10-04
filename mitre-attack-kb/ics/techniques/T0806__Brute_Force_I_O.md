# T0806: Brute Force I/O


**ATT&CK ID:** T0806  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impair Process Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0806  

## Description
Adversaries may repetitively or successively change I/O point values to perform an action. Brute Force I/O may be achieved by changing either a range of I/O point values or a single point value repeatedly to manipulate a process function. The adversary's goal and the information they have about the target environment will influence which of the options they choose. In the case of brute forcing a range of point values, the adversary may be able to achieve an impact without targeting a specific point. In the case where a single point is targeted, the adversary may be able to generate instability on the process function associated with that particular point. 

Adversaries may use Brute Force I/O to cause failures within various industrial processes. These failures could be the result of wear on equipment or damage to downstream equipment.

## Mitigations
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1157: Fuxnet
- S0604: Industroyer
- S1072: Industroyer2
