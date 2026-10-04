# T1521: Encrypted Channel


**ATT&CK ID:** T1521  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1521  

## Description
Adversaries may explicitly employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if necessary secret keys are encoded and/or generated within malware samples/configuration files.

## Sub-techniques
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1521.003: SSL Pinning

## Known Software Using This Technique
- S1095: AhRat
- S0302: Twitoor
