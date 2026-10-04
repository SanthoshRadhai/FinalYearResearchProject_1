# T1639: Exfiltration Over Alternative Protocol


**ATT&CK ID:** T1639  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1639  

## Description
Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Different protocol channels could also include Web services such as cloud storage. Adversaries may opt to also encrypt and/or obfuscate these alternate channels.

## Sub-techniques
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol

## Known Software Using This Technique
- S1056: TianySpy
