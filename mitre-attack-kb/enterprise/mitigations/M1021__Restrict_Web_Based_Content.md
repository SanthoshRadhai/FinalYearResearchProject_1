# M1021: Restrict Web-Based Content

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1021  

## Description
Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:

Deploy Web Proxy Filtering:

- Use solutions to filter web traffic based on categories, reputation, and content types.
- Enforce policies that block unsafe websites or file types at the gateway level.

Enable DNS-Based Filtering:

- Implement tools to restrict access to domains associated with malware or phishing campaigns.
- Use public DNS filtering services to enhance protection.

Enforce Content Security Policies (CSP):

- Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests.

Control Browser Features:

- Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting.
- Enforce policies through tools like Group Policy Management to control browser settings.

Monitor and Alert on Web-Based Threats:

- Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity.
- Configure alerts for access attempts to blocked domains or repeated file download failures.

## Techniques Mitigated
- T1059: Command and Scripting Interpreter
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1102: Web Service
- T1102.001: Dead Drop Resolver
- T1102.002: Bidirectional Communication
- T1102.003: One-Way Communication
- T1127: Trusted Developer Utilities Proxy Execution
- T1127.002: ClickOnce
- T1133: External Remote Services
- T1189: Drive-by Compromise
- T1204: User Execution
- T1204.001: Malicious Link
- T1204.004: Malicious Copy and Paste
- T1218: System Binary Proxy Execution
- T1218.001: Compiled HTML File
- T1528: Steal Application Access Token
- T1539: Steal Web Session Cookie
- T1550.001: Application Access Token
- T1555.003: Credentials from Web Browsers
- T1566: Phishing
- T1566.001: Spearphishing Attachment
- T1566.002: Spearphishing Link
- T1566.003: Spearphishing via Service
- T1567: Exfiltration Over Web Service
- T1567.001: Exfiltration to Code Repository
- T1567.002: Exfiltration to Cloud Storage
- T1567.003: Exfiltration to Text Storage Sites
- T1568: Dynamic Resolution
- T1568.002: Domain Generation Algorithms
- T1659: Content Injection
