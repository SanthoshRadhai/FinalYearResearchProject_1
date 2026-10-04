# S1154: VersaMem

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1154  
**Aliases:** VersaMem  
**Platforms:** Network Devices  

## Description
[VersaMem](https://attack.mitre.org/software/S1154) is a web shell designed for deployment to Versa Director servers following exploitation. Discovered in August 2024, [VersaMem](https://attack.mitre.org/software/S1154) was used during [Versa Director Zero Day Exploitation](https://attack.mitre.org/campaigns/C0039) by [Volt Typhoon](https://attack.mitre.org/groups/G1017) to target ISPs and MSPs.  [VersaMem](https://attack.mitre.org/software/S1154) is deployed as a Java Archive (JAR) and allows for credential capture for Versa Director logon activity as well as follow-on execution of arbitrary Java payloads.(Citation: Lumen Versa 2024)

## Techniques Used
- T1027.013: Encrypted/Encoded File
- T1040: Network Sniffing
- T1056.004: Credential API Hooking
- T1059: Command and Scripting Interpreter
- T1070.004: File Deletion
- T1074.001: Local Data Staging
- T1129: Shared Modules
- T1203: Exploitation for Client Execution
