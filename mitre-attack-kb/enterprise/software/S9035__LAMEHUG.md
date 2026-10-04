# S9035: LAMEHUG

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9035  
**Aliases:** LAMEHUG, PROMPTSTEAL  
**Platforms:** Windows  

## Description
[LAMEHUG](https://attack.mitre.org/software/S9035) is Python-based information stealer first identified in July 2025 by Ukraine's Computer Emergency Response Team (CERT-UA) in phishing emails targeting Ukrainian government officials. [LAMEHUG](https://attack.mitre.org/software/S9035) is the first known malware to integrate artificial intelligence (AI) directly into its attack workflow by querying large language models (LLMs) hosted on Hugging Face to dynamically generate reconnaissance, data theft, and system manipulation commands in real time.  [LAMEHUG](https://attack.mitre.org/software/S9035) has been attributed to [APT28](https://attack.mitre.org/groups/G0007). (Citation: Splunk LAMEHUG SEP 2025)(Citation: Nov AI Threat Tracker)(Citation: Cato LAMEHUG JUL 2025)

## Techniques Used
- T1005: Data from Local System
- T1007: System Service Discovery
- T1016: System Network Configuration Discovery
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1041: Exfiltration Over C2 Channel
- T1047: Windows Management Instrumentation
- T1057: Process Discovery
- T1059.003: Windows Command Shell
- T1059.006: Python
- T1069.002: Domain Groups
- T1071.001: Web Protocols
- T1074.001: Local Data Staging
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1087.002: Domain Account
- T1102.002: Bidirectional Communication
- T1119: Automated Collection
- T1132: Data Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1482: Domain Trust Discovery
- T1560.001: Archive via Utility
- T1566.001: Spearphishing Attachment
- T1573.002: Asymmetric Cryptography
