# S0604: Industroyer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0604  
**Aliases:** Industroyer, CRASHOVERRIDE, Win32/Industroyer  
**Platforms:** Windows  

## Description
[Industroyer](https://attack.mitre.org/software/S0604) is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations.(Citation: ESET Industroyer) [Industroyer](https://attack.mitre.org/software/S0604) was used in the attacks on the Ukrainian power grid in December 2016.(Citation: Dragos Crashoverride 2017) This is the first publicly known malware specifically designed to target and impact operations in the electric grid.(Citation: Dragos Crashoverride 2018)

## Techniques Used
- T1012: Query Registry
- T1016: System Network Configuration Discovery
- T1018: Remote System Discovery
- T1027: Obfuscated Files or Information
- T1041: Exfiltration Over C2 Channel
- T1046: Network Service Discovery
- T1071.001: Web Protocols
- T1078: Valid Accounts
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1090.003: Multi-hop Proxy
- T1105: Ingress Tool Transfer
- T1140: Deobfuscate/Decode Files or Information
- T1485: Data Destruction
- T1489: Service Stop
- T1499.004: Application or System Exploitation
- T1543.003: Windows Service
- T1554: Compromise Host Software Binary
- T1572: Protocol Tunneling
