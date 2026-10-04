# M1051: Update Software

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1051  

## Description
Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures:

Regular Operating System Updates

- Implementation: Apply the latest Windows security updates monthly using WSUS (Windows Server Update Services) or a similar patch management solution. Configure systems to check for updates automatically and schedule reboots during maintenance windows.
- Use Case: Prevents exploitation of OS vulnerabilities such as privilege escalation or remote code execution.

Application Patching

- Implementation: Monitor Apache's update release notes for security patches addressing vulnerabilities. Schedule updates for off-peak hours to avoid downtime while maintaining security compliance.
- Use Case: Prevents exploitation of web application vulnerabilities, such as those leading to unauthorized access or data breaches.

Firmware Updates

- Implementation: Regularly check the vendor’s website for firmware updates addressing vulnerabilities. Plan for update deployment during scheduled maintenance to minimize business disruption.
- Use Case: Protects against vulnerabilities that adversaries could exploit to gain access to network devices or inject malicious traffic.

Emergency Patch Deployment

- Implementation: Use the emergency patch deployment feature of the organization's patch management tool to apply updates to all affected Exchange servers within 24 hours.
- Use Case: Reduces the risk of exploitation by rapidly addressing critical vulnerabilities.

Centralized Patch Management

- Implementation: Implement a centralized patch management system, such as SCCM or ManageEngine, to automate and track patch deployment across all environments. Generate regular compliance reports to ensure all systems are updated.
- Use Case: Streamlines patching processes and ensures no critical systems are missed.

*Tools for Implementation*

Patch Management Tools:

- WSUS: Manage and deploy Microsoft updates across the organization.
- ManageEngine Patch Manager Plus: Automate patch deployment for OS and third-party apps.
- Ansible: Automate updates across multiple platforms, including Linux and Windows.

Vulnerability Scanning Tools:

- OpenVAS: Open-source vulnerability scanning to identify missing patches.

## Techniques Mitigated
- T1068: Exploitation for Privilege Escalation
- T1072: Software Deployment Tools
- T1110.001: Password Guessing
- T1137: Office Application Startup
- T1137.003: Outlook Forms
- T1137.004: Outlook Home Page
- T1137.005: Outlook Rules
- T1176: Software Extensions
- T1176.001: Browser Extensions
- T1176.002: IDE Extensions
- T1189: Drive-by Compromise
- T1190: Exploit Public-Facing Application
- T1195: Supply Chain Compromise
- T1195.001: Compromise Software Dependencies and Development Tools
- T1195.002: Compromise Software Supply Chain
- T1203: Exploitation for Client Execution
- T1210: Exploitation of Remote Services
- T1211: Exploitation for Stealth
- T1212: Exploitation for Credential Access
- T1495: Firmware Corruption
- T1539: Steal Web Session Cookie
- T1542: Pre-OS Boot
- T1542.001: System Firmware
- T1542.002: Component Firmware
- T1546: Event Triggered Execution
- T1546.010: AppInit DLLs
- T1546.011: Application Shimming
- T1548: Abuse Elevation Control Mechanism
- T1548.002: Bypass User Account Control
- T1550.002: Pass the Hash
- T1552: Unsecured Credentials
- T1552.006: Group Policy Preferences
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1555.005: Password Managers
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
- T1611: Escape to Host
- T1686.002: Network Device Firewall
