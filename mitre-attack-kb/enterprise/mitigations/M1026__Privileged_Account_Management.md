# M1026: Privileged Account Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1026  

## Description
Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:

Account Permissions and Roles:

- Implement RBAC and least privilege principles to allocate permissions securely.
- Use tools like Active Directory Group Policies to enforce access restrictions.

Credential Security:

- Deploy password vaulting tools like CyberArk, HashiCorp Vault, or KeePass for secure storage and rotation of credentials.
- Enforce password policies for complexity, uniqueness, and expiration using tools like Microsoft Group Policy Objects (GPO).

Multi-Factor Authentication (MFA):

- Enforce MFA for all privileged accounts using Duo Security, Okta, or Microsoft Azure AD MFA.

Privileged Access Management (PAM):

- Use PAM solutions like CyberArk, BeyondTrust, or Thycotic to manage, monitor, and audit privileged access.

Auditing and Monitoring:

- Integrate activity monitoring into your SIEM (e.g., Splunk or QRadar) to detect and alert on anomalous privileged account usage.

Just-In-Time Access:

- Deploy JIT solutions like Azure Privileged Identity Management (PIM) or configure ephemeral roles in AWS and GCP to grant time-limited elevated permissions.

*Tools for Implementation*

Privileged Access Management (PAM):

- CyberArk, BeyondTrust, Thycotic, HashiCorp Vault.

Credential Management:

- Microsoft LAPS (Local Admin Password Solution), Password Safe, HashiCorp Vault, KeePass.

Multi-Factor Authentication:

- Duo Security, Okta, Microsoft Azure MFA, Google Authenticator.

Linux Privilege Management:

- sudo configuration, SELinux, AppArmor.

Just-In-Time Access:

- Azure Privileged Identity Management (PIM), AWS IAM Roles with session constraints, GCP Identity-Aware Proxy.

## Techniques Mitigated
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1003.006: DCSync
- T1003.007: Proc Filesystem
- T1003.008: /etc/passwd and /etc/shadow
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1021.003: Distributed Component Object Model
- T1021.006: Windows Remote Management
- T1021.007: Cloud Services
- T1047: Windows Management Instrumentation
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.005: Scheduled Task
- T1053.006: Systemd Timers
- T1053.007: Container Orchestration Job
- T1055: Process Injection
- T1055.008: Ptrace System Calls
- T1056.003: Web Portal Capture
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.008: Network Device CLI
- T1059.009: Cloud API
- T1059.013: Container CLI/API
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1098.002: Additional Email Delegate Permissions
- T1098.003: Additional Cloud Roles
- T1134: Access Token Manipulation
- T1134.001: Token Impersonation/Theft
- T1134.002: Create Process with Token
- T1134.003: Make and Impersonate Token
- T1136: Create Account
- T1136.001: Local Account
- T1136.002: Domain Account
- T1136.003: Cloud Account
- T1190: Exploit Public-Facing Application
- T1210: Exploitation of Remote Services
- T1218: System Binary Proxy Execution
- T1218.007: Msiexec
- T1222: File and Directory Permissions Modification
- T1222.001: Windows Permissions
- T1222.002: Linux and Mac Permissions
- T1484: Domain or Tenant Policy Modification
- T1484.002: Trust Modification
- T1495: Firmware Corruption
- T1505: Server Software Component
- T1505.001: SQL Stored Procedures
- T1505.002: Transport Agent
- T1505.004: IIS Components
- T1525: Implant Internal Image
- T1542: Pre-OS Boot
- T1542.001: System Firmware
- T1542.003: Bootkit
- T1542.005: TFTP Boot
- T1543: Create or Modify System Process
- T1543.002: Systemd Service
- T1546: Event Triggered Execution
- T1546.003: Windows Management Instrumentation Event Subscription
- T1547.006: Kernel Modules and Extensions
- T1548: Abuse Elevation Control Mechanism
- T1548.002: Bypass User Account Control
- T1548.003: Sudo and Sudo Caching
- T1548.006: TCC Manipulation
- T1550: Use Alternate Authentication Material
- T1550.002: Pass the Hash
- T1550.003: Pass the Ticket
- T1552: Unsecured Credentials
- T1552.002: Credentials in Registry
- T1552.007: Container API
- T1553: Subvert Trust Controls
- T1553.006: Code Signing Policy Modification
- T1555: Credentials from Password Stores
- T1555.006: Cloud Secrets Management Stores
- T1556: Modify Authentication Process
- T1556.001: Domain Controller Authentication
- T1556.003: Pluggable Authentication Modules
- T1556.004: Network Device Authentication
- T1556.005: Reversible Encryption
- T1556.007: Hybrid Identity
- T1558: Steal or Forge Kerberos Tickets
- T1558.001: Golden Ticket
- T1558.002: Silver Ticket
- T1558.003: Kerberoasting
- T1559: Inter-Process Communication
- T1559.001: Component Object Model
- T1563: Remote Service Session Hijacking
- T1563.001: SSH Hijacking
- T1563.002: RDP Hijacking
- T1569: System Services
- T1569.002: Service Execution
- T1599: Network Boundary Bridging
- T1599.001: Network Address Translation Traversal
- T1601: Modify System Image
- T1601.001: Patch System Image
- T1601.002: Downgrade System Image
- T1606: Forge Web Credentials
- T1606.002: SAML Tokens
- T1609: Container Administration Command
- T1611: Escape to Host
- T1612: Build Image on Host
- T1651: Cloud Administration Command
- T1688: Safe Mode Boot
