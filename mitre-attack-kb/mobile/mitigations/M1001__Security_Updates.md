# M1001: Security Updates

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1001  

## Description
Install security updates in response to discovered vulnerabilities.

Purchase devices with a vendor and/or mobile carrier commitment to provide security updates in a prompt manner for a set period of time.

Decommission devices that will no longer receive security updates.

Limit or block access to enterprise resources from devices that have not installed recent security updates.

On Android devices, access can be controlled based on each device's security patch level. On iOS devices, access can be controlled based on the iOS version.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1404: Exploitation for Privilege Escalation
- T1456: Drive-By Compromise
- T1458: Replication Through Removable Media
- T1461: Lockscreen Bypass
- T1474: Supply Chain Compromise
- T1474.002: Compromise Hardware Supply Chain
- T1474.003: Compromise Software Supply Chain
- T1577: Compromise Application Executable
- T1629: Impair Defenses
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1630.001: Uninstall Malicious Application
- T1634: Credentials from Password Store
- T1634.001: Keychain
- T1645: Compromise Client Software Binary
- T1658: Exploitation for Client Execution
- T1664: Exploitation for Initial Access
