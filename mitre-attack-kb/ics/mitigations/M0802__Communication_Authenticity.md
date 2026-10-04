# M0802: Communication Authenticity

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0802  

## Description
When communicating over an untrusted network, utilize secure network protocols that both authenticate the message sender and can verify its integrity. This can be done either through message authentication codes (MACs) or digital signatures, to detect spoofed network messages and unauthorized connections.

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0830: Adversary-in-the-Middle
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0860: Wireless Compromise
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
