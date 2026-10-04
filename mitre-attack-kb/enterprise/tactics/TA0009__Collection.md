# TA0009: Collection

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0009  

## Description
The adversary is trying to gather data of interest to their goal.

Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary's objectives. Frequently, the next goal after collecting data is to either steal (exfiltrate) the data or to use the data to gain more information about the target environment. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

## Techniques in This Tactic
- T1005: Data from Local System
- T1025: Data from Removable Media
- T1039: Data from Network Shared Drive
- T1056: Input Capture
- T1056.001: Keylogging
- T1056.002: GUI Input Capture
- T1056.003: Web Portal Capture
- T1056.004: Credential API Hooking
- T1074: Data Staged
- T1074.001: Local Data Staging
- T1074.002: Remote Data Staging
- T1113: Screen Capture
- T1114: Email Collection
- T1114.001: Local Email Collection
- T1114.002: Remote Email Collection
- T1114.003: Email Forwarding Rule
- T1115: Clipboard Data
- T1119: Automated Collection
- T1123: Audio Capture
- T1125: Video Capture
- T1185: Browser Session Hijacking
- T1213: Data from Information Repositories
- T1213.001: Confluence
- T1213.002: Sharepoint
- T1213.003: Code Repositories
- T1213.004: Customer Relationship Management Software
- T1213.005: Messaging Applications
- T1213.006: Databases
- T1530: Data from Cloud Storage
- T1557: Adversary-in-the-Middle
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1557.002: ARP Cache Poisoning
- T1557.003: DHCP Spoofing
- T1557.004: Evil Twin
- T1560: Archive Collected Data
- T1560.001: Archive via Utility
- T1560.002: Archive via Library
- T1560.003: Archive via Custom Method
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
