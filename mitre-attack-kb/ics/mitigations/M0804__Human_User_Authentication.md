# M0804: Human User Authentication

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0804  

## Description
Require user authentication before allowing access to data or accepting commands to a device. While strong multi-factor authentication is preferable, it is not always feasible within ICS environments. Performing strong user authentication also requires additional security controls and processes which are often the target of related adversarial techniques (e.g., Valid Accounts, Default Credentials). Therefore, associated ATT&CK mitigations should be considered in addition to this, including [Multi-factor Authentication](https://attack.mitre.org/mitigations/M0932), [Account Use Policies](https://attack.mitre.org/mitigations/M0936), [Password Policies](https://attack.mitre.org/mitigations/M0927), [User Account Management](https://attack.mitre.org/mitigations/M0918), [Privileged Account Management](https://attack.mitre.org/mitigations/M0926), and [User Account Control](https://attack.mitre.org/mitigations/M1052).

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0821: Modify Controller Tasking
- T0836: Modify Parameter
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0885: Commonly Used Port
- T0886: Remote Services
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
