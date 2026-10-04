# M0807: Network Allowlists

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0807  

## Description
Network allowlists can be implemented through either host-based files or system hosts files to specify what connections (e.g., IP address, MAC address, port, protocol) can be made from a device. Allowlist techniques that operate at the  application layer (e.g., DNP3, Modbus, HTTP) are addressed in [Filter Network Traffic](https://attack.mitre.org/mitigations/M0937) mitigation.

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0869: Standard Application Layer Protocol
- T0878: Alarm Suppression
- T0879: Damage to Property
- T0884: Connection Proxy
- T0886: Remote Services
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message
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
