# M0937: Filter Network Traffic

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0937  

## Description
Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic.   Perform inline allow/denylisting of network messages based on the application layer (OSI Layer 7) protocol, especially for automation protocols. Application allowlists are beneficial when there are well-defined communication sequences, types, rates, or patterns needed during expected system operations. Application denylists may be needed if all acceptable communication sequences cannot be defined, but instead a set of known malicious uses can be denied (e.g., excessive communication  attempts, shutdown messages, invalid commands).  Devices performing these functions are often referred to as deep-packet inspection (DPI) firewalls, context-aware firewalls, or firewalls blocking specific automation/SCADA protocol aware firewalls. (Citation: Centre for the Protection of National Infrastructure February 2005)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0884: Connection Proxy
- T0886: Remote Services
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
