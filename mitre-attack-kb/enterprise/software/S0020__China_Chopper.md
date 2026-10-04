# S0020: China Chopper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0020  
**Aliases:** China Chopper  
**Platforms:** Windows  

## Description
[China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021)

## Techniques Used
- T1005: Data from Local System
- T1027.002: Software Packing
- T1046: Network Service Discovery
- T1059.003: Windows Command Shell
- T1070.006: Timestomp
- T1071.001: Web Protocols
- T1083: File and Directory Discovery
- T1105: Ingress Tool Transfer
- T1110.001: Password Guessing
- T1505.003: Web Shell
