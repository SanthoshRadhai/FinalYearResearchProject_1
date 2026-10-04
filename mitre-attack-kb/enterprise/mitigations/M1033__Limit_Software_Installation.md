# M1033: Limit Software Installation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1033  

## Description
Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures:

Application Whitelisting

- Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software.
- Whitelist applications based on file hash, path, or digital signatures.

Restrict User Permissions

- Remove local administrator rights for all non-IT users.
- Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only.

Software Restriction Policies (SRP)

- Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives.
- Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only.

Endpoint Management Solutions

- Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management.
- Maintain a list of approved software, versions, and updates across the enterprise.

Monitor Software Installation Events

- Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs.
- Use SIEM or EDR tools to alert on attempts to install unapproved software.

Implement Software Inventory Management

- Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers.
- Conduct regular audits to detect and remove unapproved software.

*Tools for Implementation*

Application Whitelisting:

- Microsoft AppLocker
- Windows Defender Application Control (WDAC)

Endpoint Management:

- Microsoft Intune
- SCCM (System Center Configuration Manager)
- Jamf Pro (macOS)
- Puppet or Ansible for automation

Software Restriction Policies:

- Group Policy Object (GPO)
- Microsoft Software Restriction Policies (SRP)

Monitoring and Logging:

- Splunk
- OSQuery
- Wazuh (open-source SIEM and XDR)
- EDRs

Inventory Management and Auditing:

- OSQuery
- Wazuh

## Techniques Mitigated
- T1021.005: VNC
- T1059: Command and Scripting Interpreter
- T1059.006: Python
- T1059.011: Lua
- T1072: Software Deployment Tools
- T1176: Software Extensions
- T1176.001: Browser Extensions
- T1176.002: IDE Extensions
- T1195: Supply Chain Compromise
- T1195.001: Compromise Software Dependencies and Development Tools
- T1204: User Execution
- T1204.005: Malicious Library
- T1543: Create or Modify System Process
- T1543.002: Systemd Service
- T1547.013: XDG Autostart Entries
- T1564: Hide Artifacts
- T1564.003: Hidden Window
