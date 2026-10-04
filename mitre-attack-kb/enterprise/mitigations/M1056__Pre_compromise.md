# M1056: Pre-compromise

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1056  

## Description
Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

Limit Information Exposure:

- Regularly audit and sanitize publicly available data, including job posts, websites, and social media.
- Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information.

Protect Domain and DNS Infrastructure:

- Enable DNSSEC and use WHOIS privacy protection.
- Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools.

External Monitoring:

- Use tools like Shodan, Censys to monitor your external attack surface.
- Deploy external vulnerability scanners to proactively address weaknesses.

Threat Intelligence:

- Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity.

Content and Email Protections:

- Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast.
- Enforce SPF/DKIM/DMARC policies to protect against email spoofing.

Training and Awareness:

- Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

## Techniques Mitigated
- T1583: Acquire Infrastructure
- T1583.001: Domains
- T1583.002: DNS Server
- T1583.003: Virtual Private Server
- T1583.004: Server
- T1583.005: Botnet
- T1583.006: Web Services
- T1583.007: Serverless
- T1583.008: Malvertising
- T1584: Compromise Infrastructure
- T1584.001: Domains
- T1584.002: DNS Server
- T1584.003: Virtual Private Server
- T1584.004: Server
- T1584.005: Botnet
- T1584.006: Web Services
- T1584.007: Serverless
- T1584.008: Network Devices
- T1585: Establish Accounts
- T1585.001: Social Media Accounts
- T1585.002: Email Accounts
- T1585.003: Cloud Accounts
- T1586: Compromise Accounts
- T1586.001: Social Media Accounts
- T1586.002: Email Accounts
- T1586.003: Cloud Accounts
- T1587: Develop Capabilities
- T1587.001: Malware
- T1587.002: Code Signing Certificates
- T1587.003: Digital Certificates
- T1587.004: Exploits
- T1588: Obtain Capabilities
- T1588.001: Malware
- T1588.002: Tool
- T1588.003: Code Signing Certificates
- T1588.004: Digital Certificates
- T1588.005: Exploits
- T1588.006: Vulnerabilities
- T1588.007: Artificial Intelligence
- T1589: Gather Victim Identity Information
- T1589.001: Credentials
- T1589.002: Email Addresses
- T1589.003: Employee Names
- T1590: Gather Victim Network Information
- T1590.001: Domain Properties
- T1590.003: Network Trust Dependencies
- T1590.004: Network Topology
- T1590.005: IP Addresses
- T1590.006: Network Security Appliances
- T1591: Gather Victim Org Information
- T1591.001: Determine Physical Locations
- T1591.002: Business Relationships
- T1591.003: Identify Business Tempo
- T1591.004: Identify Roles
- T1592: Gather Victim Host Information
- T1592.001: Hardware
- T1592.002: Software
- T1592.003: Firmware
- T1592.004: Client Configurations
- T1593.001: Social Media
- T1593.002: Search Engines
- T1594: Search Victim-Owned Websites
- T1595: Active Scanning
- T1595.001: Scanning IP Blocks
- T1595.002: Vulnerability Scanning
- T1595.003: Wordlist Scanning
- T1596: Search Open Technical Databases
- T1596.001: DNS/Passive DNS
- T1596.002: WHOIS
- T1596.003: Digital Certificates
- T1596.004: CDNs
- T1596.005: Scan Databases
- T1597: Search Closed Sources
- T1597.001: Threat Intel Vendors
- T1597.002: Purchase Technical Data
- T1608: Stage Capabilities
- T1608.001: Upload Malware
- T1608.002: Upload Tool
- T1608.003: Install Digital Certificate
- T1608.004: Drive-by Target
- T1608.005: Link Target
- T1608.006: SEO Poisoning
- T1650: Acquire Access
- T1681: Search Threat Vendor Data
- T1682: Query Public AI Services
- T1683: Generate Content
- T1683.001: Written Content
- T1683.002: Audio-Visual Content
