# S1073: Royal

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1073  
**Aliases:** Royal  
**Platforms:** Windows, ESXi  

## Description
[Royal](https://attack.mitre.org/software/S1073) is ransomware that first appeared in early 2022;  a version that also targets ESXi servers was later observed in February 2023. [Royal](https://attack.mitre.org/software/S1073) employs partial encryption and multiple threads to evade detection and speed encryption. [Royal](https://attack.mitre.org/software/S1073) has been used in attacks against multiple industries worldwide--including critical infrastructure. Security researchers have identified similarities in the encryption routines and TTPs used in [Royal](https://attack.mitre.org/software/S1073) and [Conti](https://attack.mitre.org/software/S0575) attacks and noted a possible connection between their operators.(Citation: Microsoft Royal ransomware November 2022)(Citation: Cybereason Royal December 2022)(Citation: Kroll Royal Deep Dive February 2023)(Citation: Trend Micro Royal Linux ESXi February 2023)(Citation: CISA Royal AA23-061A March 2023)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1021.002: SMB/Windows Admin Shares
- T1046: Network Service Discovery
- T1057: Process Discovery
- T1059.012: Hypervisor CLI
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1095: Non-Application Layer Protocol
- T1106: Native API
- T1135: Network Share Discovery
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1566: Phishing
- T1680: Local Storage Discovery
