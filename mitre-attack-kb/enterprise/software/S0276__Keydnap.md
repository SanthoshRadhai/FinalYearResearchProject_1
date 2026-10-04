# S0276: Keydnap

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0276  
**Aliases:** Keydnap, OSX/Keydnap  
**Platforms:** macOS  

## Description
This piece of malware steals the content of the user's keychain while maintaining a permanent backdoor  (Citation: OSX Keydnap malware).

## Techniques Used
- T1036.006: Space after Filename
- T1056.002: GUI Input Capture
- T1059.006: Python
- T1071.001: Web Protocols
- T1090.003: Multi-hop Proxy
- T1543.001: Launch Agent
- T1548.001: Setuid and Setgid
- T1555.002: Securityd Memory
- T1564.009: Resource Forking
