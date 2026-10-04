# M1037: Filter Network Traffic

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1037  

## Description
Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:

Ingress Traffic Filtering:

- Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers.
- Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges.

Egress Traffic Filtering:

- Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications.
- Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected.

Protocol-Based Filtering:

- Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs.
- Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue.

Network Segmentation:

- Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized.
- Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems.

Application Layer Filtering:

- Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic.
- Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

## Techniques Mitigated
- T1021.002: SMB/Windows Admin Shares
- T1021.005: VNC
- T1048: Exfiltration Over Alternative Protocol
- T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1071: Application Layer Protocol
- T1071.001: Web Protocols
- T1071.002: File Transfer Protocols
- T1071.003: Mail Protocols
- T1071.004: DNS
- T1071.005: Publish/Subscribe Protocols
- T1090: Proxy
- T1090.003: Multi-hop Proxy
- T1095: Non-Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1187: Forced Authentication
- T1190: Exploit Public-Facing Application
- T1197: BITS Jobs
- T1205: Traffic Signaling
- T1205.001: Port Knocking
- T1205.002: Socket Filters
- T1218: System Binary Proxy Execution
- T1218.012: Verclsid
- T1219: Remote Access Tools
- T1219.002: Remote Desktop Software
- T1498: Network Denial of Service
- T1498.001: Direct Network Flood
- T1498.002: Reflection Amplification
- T1499: Endpoint Denial of Service
- T1499.001: OS Exhaustion Flood
- T1499.002: Service Exhaustion Flood
- T1499.003: Application Exhaustion Flood
- T1499.004: Application or System Exploitation
- T1530: Data from Cloud Storage
- T1537: Transfer Data to Cloud Account
- T1552: Unsecured Credentials
- T1552.005: Cloud Instance Metadata API
- T1557: Adversary-in-the-Middle
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1557.002: ARP Cache Poisoning
- T1557.003: DHCP Spoofing
- T1570: Lateral Tool Transfer
- T1572: Protocol Tunneling
- T1599: Network Boundary Bridging
- T1599.001: Network Address Translation Traversal
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
