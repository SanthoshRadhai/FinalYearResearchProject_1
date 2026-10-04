# M1047: Audit

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1047  

## Description
Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Auditing is applicable to all systems used within an organization, from the front door of a building to accessing a file on a fileserver. It is considered more critical for regulated industries such as, healthcare, finance and government where compliance requirements demand stringent tracking of user and system activates.This mitigation can be implemented through the following measures: 

System Audit:

- Use Case: Regularly assess system configurations to ensure compliance with organizational security policies.
- Implementation: Use tools to scan for deviations from established benchmarks.

Permission Audits:

- Use Case: Review file and folder permissions to minimize the risk of unauthorized access or privilege escalation.
- Implementation: Run access reviews to identify users or groups with excessive permissions.

Software Audits:

- Use Case: Identify outdated, unsupported, or insecure software that could serve as an attack vector.
- Implementation: Use inventory and vulnerability scanning tools to detect outdated versions and recommend secure alternatives.

Configuration Audits:

- Use Case: Evaluate system and network configurations to ensure secure settings (e.g., disabled SMBv1, enabled MFA).
- Implementation: Implement automated configuration scanning tools like SCAP (Security Content Automation Protocol) to identify non-compliant systems.

Network Audits:

- Use Case: Examine network traffic, firewall rules, and endpoint communications to identify unauthorized or insecure connections.
- Implementation: Utilize tools such as Wireshark, or Zeek to monitor and log suspicious network behavior.

## Techniques Mitigated
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.005: VNC
- T1027: Obfuscated Files or Information
- T1027.011: Fileless Storage
- T1036: Masquerading
- T1036.010: Masquerade Account Name
- T1036.012: Browser Fingerprint
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1059: Command and Scripting Interpreter
- T1059.006: Python
- T1059.011: Lua
- T1070.008: Clear Mailbox Data
- T1087.004: Cloud Account
- T1095: Non-Application Layer Protocol
- T1114: Email Collection
- T1114.003: Email Forwarding Rule
- T1176: Software Extensions
- T1176.001: Browser Extensions
- T1176.002: IDE Extensions
- T1204.003: Malicious Image
- T1213: Data from Information Repositories
- T1213.001: Confluence
- T1213.002: Sharepoint
- T1213.003: Code Repositories
- T1213.004: Customer Relationship Management Software
- T1213.005: Messaging Applications
- T1213.006: Databases
- T1482: Domain Trust Discovery
- T1484: Domain or Tenant Policy Modification
- T1484.001: Group Policy Modification
- T1505: Server Software Component
- T1505.001: SQL Stored Procedures
- T1505.002: Transport Agent
- T1505.004: IIS Components
- T1505.005: Terminal Services DLL
- T1505.006: vSphere Installation Bundles
- T1525: Implant Internal Image
- T1528: Steal Application Access Token
- T1530: Data from Cloud Storage
- T1539: Steal Web Session Cookie
- T1542: Pre-OS Boot
- T1542.004: ROMMONkit
- T1542.005: TFTP Boot
- T1543: Create or Modify System Process
- T1543.003: Windows Service
- T1543.004: Launch Daemon
- T1546.006: LC_LOAD_DYLIB Addition
- T1548: Abuse Elevation Control Mechanism
- T1548.002: Bypass User Account Control
- T1548.006: TCC Manipulation
- T1550: Use Alternate Authentication Material
- T1550.001: Application Access Token
- T1552: Unsecured Credentials
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1552.004: Private Keys
- T1552.006: Group Policy Preferences
- T1552.008: Chat Messages
- T1556: Modify Authentication Process
- T1556.006: Multi-Factor Authentication
- T1556.007: Hybrid Identity
- T1556.008: Network Provider DLL
- T1558: Steal or Forge Kerberos Tickets
- T1558.004: AS-REP Roasting
- T1558.005: Ccache Files
- T1560: Archive Collected Data
- T1560.001: Archive via Utility
- T1563.002: RDP Hijacking
- T1564: Hide Artifacts
- T1564.006: Run Virtual Instance
- T1564.008: Email Hiding Rules
- T1566: Phishing
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1574.005: Executable Installer File Permissions Weakness
- T1574.007: Path Interception by PATH Environment Variable
- T1574.008: Path Interception by Search Order Hijacking
- T1574.009: Path Interception by Unquoted Path
- T1574.010: Services File Permissions Weakness
- T1578: Modify Cloud Compute Infrastructure
- T1578.001: Create Snapshot
- T1578.002: Create Cloud Instance
- T1578.003: Delete Cloud Instance
- T1578.005: Modify Cloud Compute Configurations
- T1593: Search Open Websites/Domains
- T1593.003: Code Repositories
- T1606: Forge Web Credentials
- T1606.001: Web Cookies
- T1606.002: SAML Tokens
- T1610: Deploy Container
- T1612: Build Image on Host
- T1649: Steal or Forge Authentication Certificates
- T1653: Power Settings
- T1666: Modify Cloud Resource Hierarchy
- T1671: Cloud Application Integration
- T1684: Social Engineering
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1685.004: Disable or Modify Linux Audit System Log
- T1686: Disable or Modify System Firewall
- T1686.001: Cloud Firewall
- T1686.002: Network Device Firewall
- T1686.003: Windows Host Firewall
