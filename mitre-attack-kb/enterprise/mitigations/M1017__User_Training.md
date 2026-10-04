# M1017: User Training

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1017  

## Description
User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:

Create Comprehensive Training Programs:

- Design training modules tailored to the organization's risk profile, covering topics such as phishing, password management, and incident reporting.
- Provide role-specific training for high-risk employees, such as helpdesk staff or executives.

Use Simulated Exercises:

- Conduct phishing simulations to measure user susceptibility and provide targeted follow-up training.
- Run social engineering drills to evaluate employee responses and reinforce protocols.

Leverage Gamification and Engagement:

- Introduce interactive learning methods such as quizzes, gamified challenges, and rewards for successful detection and reporting of threats.

Incorporate Security Policies into Onboarding:

- Include cybersecurity training as part of the onboarding process for new employees.
- Provide easy-to-understand materials outlining acceptable use policies and reporting procedures.

Regular Refresher Courses:

- Update training materials to include emerging threats and techniques used by adversaries.
- Ensure all employees complete periodic refresher courses to stay informed.

Emphasize Real-World Scenarios:

- Use case studies of recent attacks to demonstrate the consequences of successful phishing or social engineering.
- Discuss how specific employee actions can prevent or mitigate such attacks.

## Techniques Mitigated
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1027: Obfuscated Files or Information
- T1036: Masquerading
- T1036.007: Double File Extension
- T1056.002: GUI Input Capture
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1078.002: Domain Accounts
- T1078.004: Cloud Accounts
- T1111: Multi-Factor Authentication Interception
- T1176: Software Extensions
- T1176.001: Browser Extensions
- T1176.002: IDE Extensions
- T1185: Browser Session Hijacking
- T1189: Drive-by Compromise
- T1204: User Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1204.003: Malicious Image
- T1204.005: Malicious Library
- T1213: Data from Information Repositories
- T1213.001: Confluence
- T1213.002: Sharepoint
- T1213.003: Code Repositories
- T1213.004: Customer Relationship Management Software
- T1213.005: Messaging Applications
- T1213.006: Databases
- T1221: Template Injection
- T1528: Steal Application Access Token
- T1539: Steal Web Session Cookie
- T1547.007: Re-opened Applications
- T1552: Unsecured Credentials
- T1552.001: Credentials In Files
- T1552.008: Chat Messages
- T1555.003: Credentials from Web Browsers
- T1555.005: Password Managers
- T1556.001: Domain Controller Authentication
- T1557: Adversary-in-the-Middle
- T1557.002: ARP Cache Poisoning
- T1557.004: Evil Twin
- T1566: Phishing
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1566.004: Spearphishing Voice
- T1598: Phishing for Information
- T1598.001: Spearphishing Service
- T1598.002: Spearphishing Attachment
- T1598.003: Spearphishing Link
- T1598.004: Spearphishing Voice
- T1621: Multi-Factor Authentication Request Generation
- T1657: Financial Theft
- T1667: Email Bombing
- T1684: Social Engineering
- T1684.001: Impersonation
