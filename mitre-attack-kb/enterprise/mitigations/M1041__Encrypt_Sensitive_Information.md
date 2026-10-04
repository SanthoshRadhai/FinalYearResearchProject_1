# M1041: Encrypt Sensitive Information

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1041  

## Description
Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:

Encrypt Data at Rest:

- Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices.
- Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives.

Encrypt Data in Transit:

- Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks.
- Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption.

Encrypt Backups:

- Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access.
- Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud.

Encrypt Application Secrets:

- Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults.
- Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets.

Database Encryption:

- Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems.
- Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security numbers.

## Techniques Mitigated
- T1003: OS Credential Dumping
- T1003.003: NTDS
- T1020.001: Traffic Duplication
- T1040: Network Sniffing
- T1070: Indicator Removal
- T1114: Email Collection
- T1114.001: Local Email Collection
- T1114.002: Remote Email Collection
- T1114.003: Email Forwarding Rule
- T1119: Automated Collection
- T1213: Data from Information Repositories
- T1213.006: Databases
- T1530: Data from Cloud Storage
- T1550.001: Application Access Token
- T1552: Unsecured Credentials
- T1552.004: Private Keys
- T1557: Adversary-in-the-Middle
- T1557.002: ARP Cache Poisoning
- T1558: Steal or Forge Kerberos Tickets
- T1558.002: Silver Ticket
- T1558.003: Kerberoasting
- T1558.004: AS-REP Roasting
- T1565: Data Manipulation
- T1565.001: Stored Data Manipulation
- T1565.002: Transmitted Data Manipulation
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
- T1649: Steal or Forge Authentication Certificates
- T1659: Content Injection
- T1669: Wi-Fi Networks
- T1685.005: Clear Windows Event Logs
- T1685.006: Clear Linux or Mac System Logs
