# TA0010: Exfiltration

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0010  

## Description
The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

## Techniques in This Tactic
- T1011: Exfiltration Over Other Network Medium
- T1011.001: Exfiltration Over Bluetooth
- T1020: Automated Exfiltration
- T1020.001: Traffic Duplication
- T1029: Scheduled Transfer
- T1030: Data Transfer Size Limits
- T1041: Exfiltration Over C2 Channel
- T1048: Exfiltration Over Alternative Protocol
- T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1052: Exfiltration Over Physical Medium
- T1052.001: Exfiltration over USB
- T1537: Transfer Data to Cloud Account
- T1567: Exfiltration Over Web Service
- T1567.001: Exfiltration to Code Repository
- T1567.002: Exfiltration to Cloud Storage
- T1567.003: Exfiltration to Text Storage Sites
- T1567.004: Exfiltration Over Webhook
