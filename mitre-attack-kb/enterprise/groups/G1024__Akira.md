# G1024: Akira

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1024  
**Aliases:** Akira, GOLD SAHARA, PUNK SPIDER, Howling Scorpius  

## Description
[Akira](https://attack.mitre.org/groups/G1024) is a ransomware variant and ransomware deployment entity active since at least March 2023.(Citation: Arctic Wolf Akira 2023) [Akira](https://attack.mitre.org/groups/G1024) uses compromised credentials to access single-factor external access mechanisms such as VPNs for initial access, then various publicly-available tools and techniques for lateral movement.(Citation: Arctic Wolf Akira 2023)(Citation: Secureworks GOLD SAHARA) [Akira](https://attack.mitre.org/groups/G1024) operations are associated with "double extortion" ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Technical analysis of [Akira](https://attack.mitre.org/software/S1129) ransomware indicates variants capable of targeting Windows or VMWare ESXi hypervisors and multiple overlaps with [Conti](https://attack.mitre.org/software/S0575) ransomware.(Citation: BushidoToken Akira 2023)(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024)

## Techniques Used
- T1018: Remote System Discovery
- T1021.001: Remote Desktop Protocol
- T1027.001: Binary Padding
- T1036.005: Match Legitimate Resource Name or Location
- T1059.001: PowerShell
- T1078: Valid Accounts
- T1133: External Remote Services
- T1213.002: Sharepoint
- T1219: Remote Access Tools
- T1482: Domain Trust Discovery
- T1486: Data Encrypted for Impact
- T1531: Account Access Removal
- T1558: Steal or Forge Kerberos Tickets
- T1560.001: Archive via Utility
- T1567.002: Exfiltration to Cloud Storage
- T1657: Financial Theft
- T1685: Disable or Modify Tools
