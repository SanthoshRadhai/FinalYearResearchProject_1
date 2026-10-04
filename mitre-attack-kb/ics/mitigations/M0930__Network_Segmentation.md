# M0930: Network Segmentation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0930  

## Description
Architect sections of the network to isolate critical systems, functions, or resources. Use physical and logical segmentation to prevent access to potentially sensitive systems and information. Use a DMZ to contain any internet-facing services that should not be exposed from the internal network.  Restrict network access to only required systems and services. In addition, prevent systems from other networks or business functions (e.g., enterprise) from accessing critical process control systems. For example, in IEC 62443, systems within the same secure level should be grouped into a zone, and access to that zone is restricted by a conduit, or mechanism to restrict data flows between zones by segmenting the network. (Citation: IEC February 2019) (Citation: IEC August 2013)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0819: Exploit Public-Facing Application
- T0822: External Remote Services
- T0830: Adversary-in-the-Middle
- T0838: Modify Alarm Settings
- T0842: Network Sniffing
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0864: Transient Cyber Asset
- T0866: Exploitation of Remote Services
- T0868: Detect Operating Mode
- T0869: Standard Application Layer Protocol
- T0878: Alarm Suppression
- T0881: Service Stop
- T0883: Internet Accessible Device
- T0885: Commonly Used Port
- T0886: Remote Services
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1695: Block Communications
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi
