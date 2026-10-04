# S1218: VIRTUALPIE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1218  
**Aliases:** VIRTUALPIE  
**Platforms:** ESXi  

## Description
[VIRTUALPIE](https://attack.mitre.org/software/S1218) is a lightweight backdoor written in Python that spawns an IPv6 listener on a VMware ESXi server and features command line execution, file transfer,  and reverse shell capabilities. [VIRTUALPIE](https://attack.mitre.org/software/S1218) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who installed it via malicious vSphere Installation Bundles (VIBs).(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)

## Techniques Used
- T1059.006: Python
- T1059.012: Hypervisor CLI
- T1505.006: vSphere Installation Bundles
- T1570: Lateral Tool Transfer
- T1571: Non-Standard Port
- T1573.001: Symmetric Cryptography
