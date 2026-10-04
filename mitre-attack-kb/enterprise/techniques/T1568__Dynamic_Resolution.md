# T1568: Dynamic Resolution


**ATT&CK ID:** T1568  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1568  

## Description
Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

## Sub-techniques
- T1568.001: Fast Flux DNS
- T1568.002: Domain Generation Algorithms
- T1568.003: DNS Calculation

## Mitigations
- M1021: Restrict Web-Based Content
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G0016: APT29
- G1002: BITTER
- G0047: Gamaredon Group
- G0094: Kimsuky
- G1042: RedEcho
- G1018: TA2541
- G0134: Transparent Tribe

## Known Software Using This Technique
- S1087: AsyncRAT
- S9015: BRICKSTORM
- S0268: Bisonal
- S0666: Gelsemium
- S0449: Maze
- S0034: NETEAGLE
- S0148: RTM
- S0332: Remcos
- S0559: SUNBURST
- S0671: Tomiris
