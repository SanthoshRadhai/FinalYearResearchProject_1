# T1567: Exfiltration Over Web Service


**ATT&CK ID:** T1567  
**Domain:** Mitre Attack  
**Tactic(s):** Exfiltration  
**Platforms:** ESXi, Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1567  

## Description
Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Sub-techniques
- T1567.001: Exfiltration to Code Repository
- T1567.002: Exfiltration to Cloud Storage
- T1567.003: Exfiltration to Text Storage Sites
- T1567.004: Exfiltration Over Webhook

## Mitigations
- M1021: Restrict Web-Based Content
- M1057: Data Loss Prevention

## Known Threat Groups Using This Technique
- G0007: APT28
- G1043: BlackByte
- G1052: Contagious Interview
- G0059: Magic Hound
- G1057: ShinyHunters

## Known Software Using This Technique
- S0622: AppleSeed
- S0547: DropBook
- S1179: Exbyte
- S1245: InvisibleFerret
- S1171: OilCheck
- S1168: SampleCheck5000
- S0508: ngrok
