# M1028: Operating System Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1028  

## Description
Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 

Disable Unused Features:

- Turn off SMBv1, LLMNR, and NetBIOS where not needed.
- Disable remote registry and unnecessary services.

Enforce OS-level Protections:

- Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows.
- Use AppArmor or SELinux on Linux for mandatory access controls.

Secure Access Settings:

- Enable User Account Control (UAC) for Windows.
- Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files.

File System Hardening:

- Implement least-privilege access for critical files and system directories.
- Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS).

Secure Remote Access:

- Restrict RDP, SSH, and VNC to authorized IPs using firewall rules.
- Enable NLA for RDP and enforce strong password/lockout policies.

Harden Boot Configurations:

- Enable Secure Boot and enforce UEFI/BIOS password protection.
- Use BitLocker or LUKS to encrypt boot drives.

Regular Audits:

- Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools.

*Tools for Implementation*

Windows:

- Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings.
- Windows Defender Exploit Guard: Built-in OS protection against exploits.
- CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks.

Linux/macOS:

- AppArmor/SELinux: Enforce mandatory access controls.
- Lynis: Perform comprehensive security audits.
- SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol.

Cross-Platform:

- Ansible or Chef/Puppet: Automate configuration hardening at scale.
- OpenSCAP: Perform compliance and configuration checks.

## Techniques Mitigated
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.005: Cached Domain Credentials
- T1011: Exfiltration Over Other Network Medium
- T1011.001: Exfiltration Over Bluetooth
- T1021.001: Remote Desktop Protocol
- T1036.007: Double File Extension
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.005: Scheduled Task
- T1087: Account Discovery
- T1087.001: Local Account
- T1087.002: Domain Account
- T1092: Communication Through Removable Media
- T1098: Account Manipulation
- T1135: Network Share Discovery
- T1136: Create Account
- T1136.002: Domain Account
- T1197: BITS Jobs
- T1490: Inhibit System Recovery
- T1542.005: TFTP Boot
- T1543: Create or Modify System Process
- T1543.003: Windows Service
- T1546.008: Accessibility Features
- T1548: Abuse Elevation Control Mechanism
- T1548.001: Setuid and Setgid
- T1548.003: Sudo and Sudo Caching
- T1552: Unsecured Credentials
- T1552.003: Shell History
- T1553: Subvert Trust Controls
- T1553.004: Install Root Certificate
- T1556: Modify Authentication Process
- T1556.002: Password Filter DLL
- T1556.008: Network Provider DLL
- T1563.002: RDP Hijacking
- T1564.002: Hidden Users
- T1574.006: Dynamic Linker Hijacking
- T1690: Prevent Command History Logging
