# S0357: Impacket

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0357  
**Aliases:** Impacket  
**Platforms:** Linux, macOS, Windows  

## Description
[Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1040: Network Sniffing
- T1047: Windows Management Instrumentation
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1558.003: Kerberoasting
- T1558.005: Ccache Files
- T1569.002: Service Execution
- T1570: Lateral Tool Transfer
