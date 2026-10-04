# S0659: Diavol

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0659  
**Aliases:** Diavol  
**Platforms:** Windows  

## Description
[Diavol](https://attack.mitre.org/software/S0659) is a ransomware variant first observed in June 2021 that is capable of prioritizing file types to encrypt based on a pre-configured list of extensions defined by the attacker.  The [Diavol](https://attack.mitre.org/software/S0659) Ransomware-as-a Service (RaaS) program is managed by [Wizard Spider](https://attack.mitre.org/groups/G0102) and it has been observed being deployed by [Bazar](https://attack.mitre.org/software/S0534).(Citation: Fortinet Diavol July 2021)(Citation: FBI Flash Diavol January 2022)(Citation: DFIR Diavol Ransomware December 2021)(Citation: Microsoft Ransomware as a Service)

## Techniques Used
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1021.002: SMB/Windows Admin Shares
- T1027: Obfuscated Files or Information
- T1027.003: Steganography
- T1033: System Owner/User Discovery
- T1057: Process Discovery
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1106: Native API
- T1135: Network Share Discovery
- T1485: Data Destruction
- T1486: Data Encrypted for Impact
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1491.001: Internal Defacement
- T1685: Disable or Modify Tools
