# M0801: Access Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0801  

## Description
Access Management technologies can be used to enforce authorization polices and decisions, especially when existing field devices do not provide sufficient capabilities to support user identification and authentication. (Citation: McCarthy, J et al. July 2018) These technologies typically utilize an in-line network device or gateway system to prevent access to unauthenticated users, while also integrating with an authentication service to first verify user credentials. (Citation: Centre for the Protection of National Infrastructure November 2010)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0886: Remote Services
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1694: Insecure Credentials
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials
