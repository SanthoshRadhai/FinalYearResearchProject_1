# M1018: User Account Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1018  

## Description
User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:

Enforcing the Principle of Least Privilege

- Implementation: Assign users only the minimum permissions required to perform their job functions. Regularly audit accounts to ensure no excess permissions are granted.
- Use Case: Reduces the risk of privilege escalation by ensuring accounts cannot perform unauthorized actions.

Implementing Strong Password Policies

- Implementation: Enforce password complexity requirements (e.g., length, character types). Require password expiration every 90 days and disallow password reuse.
- Use Case: Prevents adversaries from gaining unauthorized access through password guessing or brute force attacks.

Managing Dormant and Orphaned Accounts

- Implementation: Implement automated workflows to disable accounts after a set period of inactivity (e.g., 30 days). Remove orphaned accounts (e.g., accounts without an assigned owner) during regular account audits.
- Use Case: Eliminates dormant accounts that could be exploited by attackers.

Account Lockout Policies

- Implementation: Configure account lockout thresholds (e.g., lock accounts after five failed login attempts). Set lockout durations to a minimum of 15 minutes.
- Use Case: Mitigates automated attack techniques that rely on repeated login attempts.

Multi-Factor Authentication (MFA) for High-Risk Accounts

- Implementation: Require MFA for all administrative accounts and high-risk users. Use MFA mechanisms like hardware tokens, authenticator apps, or biometrics.
- Use Case: Prevents unauthorized access, even if credentials are stolen.

Restricting Interactive Logins

- Implementation: Restrict interactive logins for privileged accounts to specific secure systems or management consoles. Use group policies to enforce logon restrictions.
- Use Case: Protects sensitive accounts from misuse or exploitation.

*Tools for Implementation*

Built-in Tools:

- Microsoft Active Directory (AD): Centralized account management and RBAC enforcement.
- Group Policy Object (GPO): Enforce password policies, logon restrictions, and account lockout policies.

Identity and Access Management (IAM) Tools:

- Okta: Centralized user provisioning, MFA, and SSO integration.
- Microsoft Azure Active Directory: Provides advanced account lifecycle management, role-based access, and conditional access policies.

Privileged Account Management (PAM):
- CyberArk, BeyondTrust, Thycotic: Manage and monitor privileged account usage, enforce session recording, and JIT access.

## Techniques Mitigated
- T1006: Direct Volume Access
- T1020.001: Traffic Duplication
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1021.008: Direct Cloud VM Connections
- T1036: Masquerading
- T1036.010: Masquerade Account Name
- T1040: Network Sniffing
- T1047: Windows Management Instrumentation
- T1048: Exfiltration Over Alternative Protocol
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1053.006: Systemd Timers
- T1053.007: Container Orchestration Job
- T1059.008: Network Device CLI
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts
- T1087: Account Discovery
- T1087.004: Cloud Account
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1098.003: Additional Cloud Roles
- T1098.004: SSH Authorized Keys
- T1098.006: Additional Container Cluster Roles
- T1110: Brute Force
- T1110.004: Credential Stuffing
- T1134: Access Token Manipulation
- T1134.001: Token Impersonation/Theft
- T1134.002: Create Process with Token
- T1134.003: Make and Impersonate Token
- T1185: Browser Session Hijacking
- T1195: Supply Chain Compromise
- T1197: BITS Jobs
- T1199: Trusted Relationship
- T1213: Data from Information Repositories
- T1213.001: Confluence
- T1213.002: Sharepoint
- T1213.003: Code Repositories
- T1213.004: Customer Relationship Management Software
- T1213.006: Databases
- T1484: Domain or Tenant Policy Modification
- T1484.001: Group Policy Modification
- T1484.002: Trust Modification
- T1485: Data Destruction
- T1485.001: Lifecycle-Triggered Deletion
- T1489: Service Stop
- T1490: Inhibit System Recovery
- T1505: Server Software Component
- T1505.003: Web Shell
- T1528: Steal Application Access Token
- T1530: Data from Cloud Storage
- T1537: Transfer Data to Cloud Account
- T1538: Cloud Service Dashboard
- T1543: Create or Modify System Process
- T1543.002: Systemd Service
- T1543.003: Windows Service
- T1543.004: Launch Daemon
- T1543.005: Container Service
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.004: Winlogon Helper DLL
- T1547.006: Kernel Modules and Extensions
- T1547.009: Shortcut Modification
- T1547.012: Print Processors
- T1547.013: XDG Autostart Entries
- T1548: Abuse Elevation Control Mechanism
- T1548.005: Temporary Elevated Cloud Access
- T1550: Use Alternate Authentication Material
- T1550.002: Pass the Hash
- T1550.003: Pass the Ticket
- T1552.007: Container API
- T1555.003: Credentials from Web Browsers
- T1555.005: Password Managers
- T1556: Modify Authentication Process
- T1556.006: Multi-Factor Authentication
- T1556.009: Conditional Access Policies
- T1563: Remote Service Session Hijacking
- T1563.002: RDP Hijacking
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1569: System Services
- T1569.001: Launchctl
- T1569.003: Systemctl
- T1574: Hijack Execution Flow
- T1574.005: Executable Installer File Permissions Weakness
- T1574.010: Services File Permissions Weakness
- T1574.012: COR_PROFILER
- T1578: Modify Cloud Compute Infrastructure
- T1578.001: Create Snapshot
- T1578.002: Create Cloud Instance
- T1578.003: Delete Cloud Instance
- T1578.005: Modify Cloud Compute Configurations
- T1580: Cloud Infrastructure Discovery
- T1606: Forge Web Credentials
- T1606.002: SAML Tokens
- T1609: Container Administration Command
- T1610: Deploy Container
- T1613: Container and Resource Discovery
- T1619: Cloud Storage Object Discovery
- T1648: Serverless Execution
- T1654: Log Enumeration
- T1657: Financial Theft
- T1666: Modify Cloud Resource Hierarchy
- T1675: ESXi Administration Command
- T1677: Poisoned Pipeline Execution
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1685.002: Disable or Modify Cloud Log
- T1685.004: Disable or Modify Linux Audit System Log
- T1686: Disable or Modify System Firewall
- T1686.001: Cloud Firewall
- T1686.002: Network Device Firewall
- T1686.003: Windows Host Firewall
