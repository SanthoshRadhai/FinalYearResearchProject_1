# T1481: Web Service


**ATT&CK ID:** T1481  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1481  

## Description
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

 

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis, or enable operational resiliency (since this infrastructure may be dynamically changed).

## Sub-techniques
- T1481.001: Dead Drop Resolver
- T1481.002: Bidirectional Communication
- T1481.003: One-Way Communication

## Known Software Using This Technique
- S1214: Android/SpyAgent
