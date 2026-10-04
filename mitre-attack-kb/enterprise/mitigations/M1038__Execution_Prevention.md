# M1038: Execution Prevention

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1038  

## Description
Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:

Application Control:

- Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution.
- Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) 


Script Blocking:

- Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources.
- Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) 

Executable Blocking:

- Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories.
- Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories.

Dynamic Analysis Prevention:
- Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time.
- Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

## Techniques Mitigated
- T1036: Masquerading
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1047: Windows Management Instrumentation
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.002: AppleScript
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1059.008: Network Device CLI
- T1059.009: Cloud API
- T1059.010: AutoHotKey & AutoIT
- T1059.011: Lua
- T1059.013: Container CLI/API
- T1068: Exploitation for Privilege Escalation
- T1080: Taint Shared Content
- T1106: Native API
- T1127: Trusted Developer Utilities Proxy Execution
- T1127.001: MSBuild
- T1127.003: JamPlus
- T1129: Shared Modules
- T1176: Software Extensions
- T1176.001: Browser Extensions
- T1176.002: IDE Extensions
- T1204: User Execution
- T1204.002: Malicious File
- T1204.004: Malicious Copy and Paste
- T1216: System Script Proxy Execution
- T1216.001: PubPrn
- T1216.002: SyncAppvPublishingServer
- T1218: System Binary Proxy Execution
- T1218.001: Compiled HTML File
- T1218.002: Control Panel
- T1218.003: CMSTP
- T1218.004: InstallUtil
- T1218.005: Mshta
- T1218.008: Odbcconf
- T1218.009: Regsvcs/Regasm
- T1218.012: Verclsid
- T1218.013: Mavinject
- T1218.014: MMC
- T1218.015: Electron Applications
- T1219: Remote Access Tools
- T1219.001: IDE Tunneling
- T1219.002: Remote Desktop Software
- T1220: XSL Script Processing
- T1490: Inhibit System Recovery
- T1505.004: IIS Components
- T1546.002: Screensaver
- T1546.006: LC_LOAD_DYLIB Addition
- T1546.008: Accessibility Features
- T1546.009: AppCert DLLs
- T1546.010: AppInit DLLs
- T1547.004: Winlogon Helper DLL
- T1547.006: Kernel Modules and Extensions
- T1547.009: Shortcut Modification
- T1548: Abuse Elevation Control Mechanism
- T1548.004: Elevated Execution with Prompt
- T1553: Subvert Trust Controls
- T1553.001: Gatekeeper Bypass
- T1553.003: SIP and Trust Provider Hijacking
- T1553.005: Mark-of-the-Web Bypass
- T1564.003: Hidden Window
- T1564.006: Run Virtual Instance
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1574.006: Dynamic Linker Hijacking
- T1574.007: Path Interception by PATH Environment Variable
- T1574.008: Path Interception by Search Order Hijacking
- T1574.009: Path Interception by Unquoted Path
- T1574.012: COR_PROFILER
- T1609: Container Administration Command
- T1611: Escape to Host
- T1674: Input Injection
- T1685: Disable or Modify Tools
- T1685.003: Modify or Spoof Tool UI
