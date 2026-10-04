# S0561: GuLoader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0561  
**Aliases:** GuLoader  
**Platforms:** Windows  

## Description
[GuLoader](https://attack.mitre.org/software/S0561) is a file downloader that has been used since at least December 2019 to distribute a variety of remote administration tool (RAT) malware, including [NETWIRE](https://attack.mitre.org/software/S0198), [Agent Tesla](https://attack.mitre.org/software/S0331), [NanoCore](https://attack.mitre.org/software/S0336), FormBook, and Parallax RAT.(Citation: Unit 42 NETWIRE April 2020)(Citation: Medium Eli Salem GuLoader April 2021)

## Techniques Used
- T1055: Process Injection
- T1070.004: File Deletion
- T1071.001: Web Protocols
- T1102: Web Service
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1497.001: System Checks
- T1497.003: Time Based Checks
- T1547.001: Registry Run Keys / Startup Folder
- T1566.002: Spearphishing Link
