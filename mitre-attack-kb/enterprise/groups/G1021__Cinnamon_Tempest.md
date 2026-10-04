# G1021: Cinnamon Tempest

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1021  
**Aliases:** Cinnamon Tempest, DEV-0401, Emperor Dragonfly, BRONZE STARLIGHT  

## Description
[Cinnamon Tempest](https://attack.mitre.org/groups/G1021) is a China-based threat group that has been active since at least 2021 deploying multiple strains of ransomware based on the leaked [Babuk](https://attack.mitre.org/software/S0638) source code. [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) does not operate their ransomware on an affiliate model or purchase access but appears to act independently in all stages of the attack lifecycle. Based on victimology, the short lifespan of each ransomware variant, and use of malware attributed to government-sponsored threat groups, [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) may be motivated by intellectual property theft or cyberespionage rather than financial gain.(Citation: Microsoft Ransomware as a Service)(Citation: Microsoft Threat Actor Naming July 2023)(Citation: Trend Micro Cheerscrypt May 2022)(Citation: SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022)

## Techniques Used
- T1021.002: SMB/Windows Admin Shares
- T1047: Windows Management Instrumentation
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1080: Taint Shared Content
- T1090: Proxy
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1190: Exploit Public-Facing Application
- T1484.001: Group Policy Modification
- T1543.003: Windows Service
- T1567.002: Exfiltration to Cloud Storage
- T1572: Protocol Tunneling
- T1574.001: DLL
- T1588.002: Tool
- T1657: Financial Theft
