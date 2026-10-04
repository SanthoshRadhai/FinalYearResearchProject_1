# M1024: Restrict Registry Permissions

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1024  

## Description
Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:

Review and Adjust Permissions on Critical Keys

- Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.
- Use tools like `icacls` or `PowerShell` to automate permission adjustments.

Enable Registry Auditing

- Enable auditing on sensitive keys to log access attempts.
- Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity.
- Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable`

Protect Credential-Related Hives

- Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access.
- Use LSA Protection to add an additional security layer for credential storage.

Restrict Registry Editor Usage

- Use Group Policy to restrict access to regedit.exe for non-administrative users.
- Block execution of registry editing tools on endpoints where they are unnecessary.

Deploy Baseline Configuration Tools

- Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations.

*Tools for Implementation* 

Registry Permission Tools:

- Registry Editor (regedit): Built-in tool to manage registry permissions.
- PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"`
- icacls: Command-line tool to modify ACLs.

Monitoring Tools:

- Sysmon: Monitor and log registry events.
- Event Viewer: View registry access logs.

Policy Management Tools:

- Group Policy Management Console (GPMC): Enforce registry permissions via GPOs.
- Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

## Techniques Mitigated
- T1037: Boot or Logon Initialization Scripts
- T1037.001: Logon Script (Windows)
- T1070.007: Clear Network Connection History and Configurations
- T1112: Modify Registry
- T1489: Service Stop
- T1505: Server Software Component
- T1505.005: Terminal Services DLL
- T1547.003: Time Providers
- T1553: Subvert Trust Controls
- T1553.003: SIP and Trust Provider Hijacking
- T1553.006: Code Signing Policy Modification
- T1556: Modify Authentication Process
- T1556.008: Network Provider DLL
- T1574: Hijack Execution Flow
- T1574.011: Services Registry Permissions Weakness
- T1574.012: COR_PROFILER
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1686: Disable or Modify System Firewall
- T1686.003: Windows Host Firewall
