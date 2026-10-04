# S0575: Conti

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0575  
**Aliases:** Conti  
**Platforms:** Windows  

## Description
[Conti](https://attack.mitre.org/software/S0575) is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. [Conti](https://attack.mitre.org/software/S0575) has been deployed via [TrickBot](https://attack.mitre.org/software/S0266) and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using [Conti](https://attack.mitre.org/software/S0575) steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.(Citation: Cybereason Conti Jan 2021)(Citation: CarbonBlack Conti July 2020)(Citation: Cybleinc Conti January 2020)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027: Obfuscated Files or Information
- T1049: System Network Connections Discovery
- T1055.001: Dynamic-link Library Injection
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1080: Taint Shared Content
- T1083: File and Directory Discovery
- T1106: Native API
- T1135: Network Share Discovery
- T1140: Deobfuscate/Decode Files or Information
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
