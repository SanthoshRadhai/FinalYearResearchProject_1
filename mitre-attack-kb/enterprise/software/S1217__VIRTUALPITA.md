# S1217: VIRTUALPITA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1217  
**Aliases:** VIRTUALPITA  
**Platforms:** ESXi, Linux  

## Description
[VIRTUALPITA](https://attack.mitre.org/software/S1217) is a passive backdoor with ESXi and Linux vCenter variants capable of command execution, file transfer, and starting and stopping processes. [VIRTUALPITA](https://attack.mitre.org/software/S1217) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who leveraged malicious vSphere Installation Bundles (VIBs) for install on ESXi hypervisors.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)

## Techniques Used
- T1036.004: Masquerade Task or Service
- T1036.005: Match Legitimate Resource Name or Location
- T1037: Boot or Logon Initialization Scripts
- T1059.004: Unix Shell
- T1059.006: Python
- T1105: Ingress Tool Transfer
- T1489: Service Stop
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1673: Virtual Machine Discovery
- T1675: ESXi Administration Command
- T1690: Prevent Command History Logging
