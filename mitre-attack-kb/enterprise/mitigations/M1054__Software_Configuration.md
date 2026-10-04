# M1054: Software Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1054  

## Description
Software configuration refers to making security-focused adjustments to the settings of applications, middleware, databases, or other software to mitigate potential threats. These changes help reduce the attack surface, enforce best practices, and protect sensitive data. This mitigation can be implemented through the following measures:

Conduct a Security Review of Application Settings:

- Review the software documentation to identify recommended security configurations.
- Compare default settings against organizational policies and compliance requirements.

Implement Access Controls and Permissions:

- Restrict access to sensitive features or data within the software.
- Enforce least privilege principles for all roles and accounts interacting with the software.

Enable Logging and Monitoring:

- Configure detailed logging for key application events such as authentication failures, configuration changes, or unusual activity.
- Integrate logs with a centralized monitoring solution, such as a SIEM.

Update and Patch Software Regularly:

- Ensure the software is kept up-to-date with the latest security patches to address known vulnerabilities.
- Use automated patch management tools to streamline the update process.

Disable Unnecessary Features or Services:

- Turn off unused functionality or components that could introduce vulnerabilities, such as debugging interfaces or deprecated APIs.

Test Configuration Changes:

- Perform configuration changes in a staging environment before applying them in production.
- Conduct regular audits to ensure that settings remain aligned with security policies.

*Tools for Implementation*

Configuration Management Tools:

- Ansible: Automates configuration changes across multiple applications and environments.
- Chef: Ensures consistent application settings through code-based configuration management.
- Puppet: Automates software configurations and audits changes for compliance.

Security Benchmarking Tools:

- CIS-CAT: Provides benchmarks and audits for secure software configurations.
- Aqua Security Trivy: Scans containerized applications for configuration issues.

Vulnerability Management Solutions:

- Nessus: Identifies misconfigurations and suggests corrective actions.

Logging and Monitoring Tools:

- Splunk: Aggregates and analyzes application logs to detect suspicious activity.

## Techniques Mitigated
- T1137: Office Application Startup
- T1137.002: Office Test
- T1213: Data from Information Repositories
- T1213.004: Customer Relationship Management Software
- T1213.006: Databases
- T1535: Unused/Unsupported Cloud Regions
- T1537: Transfer Data to Cloud Account
- T1539: Steal Web Session Cookie
- T1543: Create or Modify System Process
- T1543.005: Container Service
- T1546.013: PowerShell Profile
- T1550.004: Web Session Cookie
- T1553: Subvert Trust Controls
- T1553.004: Install Root Certificate
- T1555.005: Password Managers
- T1559: Inter-Process Communication
- T1559.002: Dynamic Data Exchange
- T1566: Phishing
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1590.002: DNS
- T1598: Phishing for Information
- T1598.002: Spearphishing Attachment
- T1598.003: Spearphishing Link
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
- T1606: Forge Web Credentials
- T1606.001: Web Cookies
- T1666: Modify Cloud Resource Hierarchy
- T1667: Email Bombing
- T1677: Poisoned Pipeline Execution
- T1684.002: Email Spoofing
- T1685: Disable or Modify Tools
- T1688: Safe Mode Boot
- T1689: Downgrade Attack
