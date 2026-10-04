# T1573: Encrypted Channel


**ATT&CK ID:** T1573  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1573  

## Description
Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Sub-techniques
- T1573.001: Symmetric Cryptography
- T1573.002: Asymmetric Cryptography

## Mitigations
- M1020: SSL/TLS Inspection
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0016: APT29
- G1002: BITTER
- G0059: Magic Hound
- G0081: Tropic Trooper

## Known Software Using This Technique
- S0631: Chaes
- S0498: Cryptoistic
- S0367: Emotet
- S1198: Gomir
- S0681: Lizar
- S1016: MacMa
- S0198: NETWIRE
- S1046: PowGoop
- S1012: PowerLess
- S0662: RCSession
- S0032: gh0st RAT
