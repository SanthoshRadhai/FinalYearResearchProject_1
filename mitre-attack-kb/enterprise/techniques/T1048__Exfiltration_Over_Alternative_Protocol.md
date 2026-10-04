# T1048: Exfiltration Over Alternative Protocol


**ATT&CK ID:** T1048  
**Domain:** Mitre Attack  
**Tactic(s):** Exfiltration  
**Platforms:** ESXi, IaaS, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1048  

## Description
Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. 

[Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048) can be done using various common operating system utilities such as [Net](https://attack.mitre.org/software/S0039)/SMB or FTP.(Citation: Palo Alto OilRig Oct 2016) On macOS and Linux <code>curl</code> may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.(Citation: 20 macOS Common Tools and Techniques)

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or [Cloud API](https://attack.mitre.org/techniques/T1059/009).

## Sub-techniques
- T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic
- M1057: Data Loss Prevention

## Known Threat Groups Using This Technique
- G1040: Play
- G0139: TeamTNT

## Known Software Using This Technique
- S0677: AADInternals
- S0482: Bundlore
- S0631: Chaes
- S0503: FrameworkPOS
- S0203: Hydraq
- S0641: Kobalos
- S0428: PoetRAT
