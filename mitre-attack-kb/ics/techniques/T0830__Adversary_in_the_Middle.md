# T0830: Adversary-in-the-Middle


**ATT&CK ID:** T0830  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0830  

## Description
Adversaries with privileged network access may seek to modify network traffic in real time using adversary-in-the-middle (AiTM) attacks. (Citation: Gabriel Sanchez October 2017) This type of attack allows the adversary to intercept traffic to and/or from a particular device on the network. If a AiTM attack is established, then the adversary has the ability to block, log, modify, or inject traffic into the communication stream. There are several ways to accomplish this attack, but some of the most-common are Address Resolution Protocol (ARP) poisoning and the use of a proxy. (Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)  

An AiTM attack may allow an adversary to perform the following attacks:  
[Block Reporting Message](https://attack.mitre.org/techniques/T0804), [Spoof Reporting Message](https://attack.mitre.org/techniques/T0856), [Modify Parameter](https://attack.mitre.org/techniques/T0836), [Unauthorized Command Message](https://attack.mitre.org/techniques/T0855)

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0813: Software Process and Device Authentication
- M0814: Static Network Configuration
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention
- M0942: Disable or Remove Feature or Program
- M0947: Audit

## Known Software Using This Technique
- S1010: VPNFilter
