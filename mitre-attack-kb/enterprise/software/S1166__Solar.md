# S1166: Solar

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1166  
**Aliases:** Solar  
**Platforms:** Windows  

## Description
[Solar](https://attack.mitre.org/software/S1166) is a C#/.NET backdoor that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Outer Space](https://attack.mitre.org/campaigns/C0042) campaign to download, execute, and exfiltrate files.(Citation: ESET OilRig Campaigns Sep 2023)

## Techniques Used
- T1020: Automated Exfiltration
- T1041: Exfiltration Over C2 Channel
- T1053.005: Scheduled Task
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1105: Ingress Tool Transfer
- T1132.001: Standard Encoding
- T1573.001: Symmetric Cryptography
