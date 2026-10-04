# M1022: Restrict File and Directory Permissions

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1022  

## Description
Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Enforce Least Privilege Permissions:

- Remove unnecessary write permissions on sensitive files and directories.
- Use file ownership and groups to control access for specific roles.

Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs.

Harden File Shares:

- Disable anonymous access to shared folders.
- Enforce NTFS permissions for shared folders on Windows.

Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access.

On Linux, apply:
`chmod 750 /etc/sensitive.conf`
`chown root:admin /etc/sensitive.conf`

File Integrity Monitoring (FIM):

- Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions.

Audit File System Access:

- Enable auditing to track permission changes or unauthorized access attempts.
- Use auditd (Linux) or Event Viewer (Windows) to log activities.

Restrict Startup Directories:

- Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`.

Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`.

- On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F`
- On Linux, monitor permissions using tools like `lsattr` or `auditd`.

## Techniques Mitigated
- T1036: Masquerading
- T1036.003: Rename Legitimate Utilities
- T1036.005: Match Legitimate Resource Name or Location
- T1037: Boot or Logon Initialization Scripts
- T1037.002: Login Hook
- T1037.003: Network Logon Script
- T1037.004: RC Scripts
- T1037.005: Startup Items
- T1048: Exfiltration Over Alternative Protocol
- T1053: Scheduled Task/Job
- T1053.006: Systemd Timers
- T1055.009: Proc Memory
- T1070: Indicator Removal
- T1070.003: Clear Command History
- T1070.008: Clear Mailbox Data
- T1070.009: Clear Persistence
- T1080: Taint Shared Content
- T1098: Account Manipulation
- T1098.004: SSH Authorized Keys
- T1218.002: Control Panel
- T1222: File and Directory Permissions Modification
- T1222.001: Windows Permissions
- T1222.002: Linux and Mac Permissions
- T1489: Service Stop
- T1530: Data from Cloud Storage
- T1543: Create or Modify System Process
- T1543.001: Launch Agent
- T1543.002: Systemd Service
- T1546.004: Unix Shell Configuration Modification
- T1546.013: PowerShell Profile
- T1547.003: Time Providers
- T1547.009: Shortcut Modification
- T1547.013: XDG Autostart Entries
- T1548: Abuse Elevation Control Mechanism
- T1548.003: Sudo and Sudo Caching
- T1548.006: TCC Manipulation
- T1552: Unsecured Credentials
- T1552.001: Credentials In Files
- T1552.004: Private Keys
- T1553.003: SIP and Trust Provider Hijacking
- T1556: Modify Authentication Process
- T1563.001: SSH Hijacking
- T1564.004: NTFS File Attributes
- T1565: Data Manipulation
- T1565.001: Stored Data Manipulation
- T1565.003: Runtime Data Manipulation
- T1569: System Services
- T1569.002: Service Execution
- T1574: Hijack Execution Flow
- T1574.004: Dylib Hijacking
- T1574.007: Path Interception by PATH Environment Variable
- T1574.008: Path Interception by Search Order Hijacking
- T1574.009: Path Interception by Unquoted Path
- T1574.014: AppDomainManager
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1685.005: Clear Windows Event Logs
- T1685.006: Clear Linux or Mac System Logs
- T1686: Disable or Modify System Firewall
- T1686.003: Windows Host Firewall
