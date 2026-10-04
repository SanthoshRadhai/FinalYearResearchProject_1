# G1031: Saint Bear

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1031  
**Aliases:** Saint Bear, Storm-0587, TA471, UAC-0056, Lorec53  

## Description
[Saint Bear](https://attack.mitre.org/groups/G1031) is a Russian-nexus threat actor active since early 2021, primarily targeting entities in Ukraine and Georgia. The group is notable for a specific remote access tool, [Saint Bot](https://attack.mitre.org/software/S1018), and information stealer, [OutSteel](https://attack.mitre.org/software/S1017) in campaigns. [Saint Bear](https://attack.mitre.org/groups/G1031) typically relies on phishing or web staging of malicious documents and related file types for initial access, spoofing government or related entities.(Citation: Palo Alto Unit 42 OutSteel SaintBot February 2022 )(Citation: Cadet Blizzard emerges as novel threat actor) [Saint Bear](https://attack.mitre.org/groups/G1031) has previously been confused with [Ember Bear](https://attack.mitre.org/groups/G1003) operations, but analysis of behaviors, tools, and targeting indicates these are distinct clusters.

## Techniques Used
- T1027.002: Software Packing
- T1027.013: Encrypted/Encoded File
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.003: Windows Command Shell
- T1059.007: JavaScript
- T1112: Modify Registry
- T1203: Exploitation for Client Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1497: Virtualization/Sandbox Evasion
- T1553.002: Code Signing
- T1566.001: Spearphishing Attachment
- T1583.006: Web Services
- T1589.002: Email Addresses
- T1608.001: Upload Malware
- T1684.001: Impersonation
- T1685: Disable or Modify Tools
