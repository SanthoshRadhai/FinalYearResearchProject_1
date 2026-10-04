# S1045: INCONTROLLER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1045  
**Aliases:** INCONTROLLER, PIPEDREAM  
**Platforms:** Engineering Workstation, Field Controller/RTU/PLC/IED, Safety Instrumented System/Protection Relay, Windows  

## Description
[INCONTROLLER](https://attack.mitre.org/software/S1045) is custom malware that includes multiple modules tailored towards ICS devices and technologies, including Schneider Electric and Omron PLCs as well as OPC UA, Modbus, and CODESYS protocols. [INCONTROLLER](https://attack.mitre.org/software/S1045) has the ability to discover specific devices, download logic on the devices, and exploit platform-specific vulnerabilities. As of September 2022, some security researchers assessed [INCONTROLLER](https://attack.mitre.org/software/S1045) was developed by CHERNOVITE.(Citation: CISA-AA22-103A)(Citation: Brubaker-Incontroller)(Citation: Dragos-Pipedream)(Citation: Schneider-Incontroller)(Citation: Wylie-22)

## Techniques Used
- T0809: Data Destruction
- T0836: Modify Parameter
- T0842: Network Sniffing
- T0843: Program Download
- T0843.001: Download All
- T0845: Program Upload
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.003: Multicast Discovery
- T0858: Change Operating Mode
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0867: Lateral Tool Transfer
- T0869: Standard Application Layer Protocol
- T0884: Connection Proxy
- T0886: Remote Services
- T0888: Remote System Information Discovery
- T0890: Exploitation for Privilege Escalation
- T1692.001: Command Message
- T1694.002: Hardcoded Credentials
