# M1042: Disable or Remove Feature or Program

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1042  

## Description
Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 

Remove Legacy Software:

- Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash).
- Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date.

Disable Unused Features:

- Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required.
- Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue.

Control Applications Installed by Users:

- Use Case: Prevent users from installing unauthorized software via group policies or other management tools.
- Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment.

Remove Unnecessary Services:

- Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices.
- Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations.

Restrict Add-ons and Plugins:

- Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes.
- Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.

## Techniques Mitigated
- T1011: Exfiltration Over Other Network Medium
- T1011.001: Exfiltration Over Bluetooth
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.003: Distributed Component Object Model
- T1021.004: SSH
- T1021.005: VNC
- T1021.006: Windows Remote Management
- T1021.008: Direct Cloud VM Connections
- T1046: Network Service Discovery
- T1052: Exfiltration Over Physical Medium
- T1052.001: Exfiltration over USB
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1091: Replication Through Removable Media
- T1092: Communication Through Removable Media
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1098.002: Additional Email Delegate Permissions
- T1098.004: SSH Authorized Keys
- T1114.003: Email Forwarding Rule
- T1127: Trusted Developer Utilities Proxy Execution
- T1127.001: MSBuild
- T1127.002: ClickOnce
- T1127.003: JamPlus
- T1133: External Remote Services
- T1137: Office Application Startup
- T1137.001: Office Template Macros
- T1205: Traffic Signaling
- T1210: Exploitation of Remote Services
- T1218: System Binary Proxy Execution
- T1218.003: CMSTP
- T1218.004: InstallUtil
- T1218.005: Mshta
- T1218.007: Msiexec
- T1218.008: Odbcconf
- T1218.009: Regsvcs/Regasm
- T1218.012: Verclsid
- T1218.013: Mavinject
- T1218.014: MMC
- T1218.015: Electron Applications
- T1219: Remote Access Tools
- T1219.002: Remote Desktop Software
- T1221: Template Injection
- T1505: Server Software Component
- T1505.003: Web Shell
- T1546.002: Screensaver
- T1546.014: Emond
- T1547.007: Re-opened Applications
- T1552.005: Cloud Instance Metadata API
- T1553.005: Mark-of-the-Web Bypass
- T1555.004: Windows Credential Manager
- T1557: Adversary-in-the-Middle
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1557.002: ARP Cache Poisoning
- T1559: Inter-Process Communication
- T1559.002: Dynamic Data Exchange
- T1563: Remote Service Session Hijacking
- T1563.001: SSH Hijacking
- T1563.002: RDP Hijacking
- T1564.006: Run Virtual Instance
- T1564.007: VBA Stomping
- T1595.003: Wordlist Scanning
- T1609: Container Administration Command
- T1611: Escape to Host
- T1649: Steal or Forge Authentication Certificates
- T1671: Cloud Application Integration
- T1685: Disable or Modify Tools
- T1689: Downgrade Attack
