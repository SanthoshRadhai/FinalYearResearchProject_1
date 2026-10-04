# M1030: Network Segmentation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1030  

## Description
Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.

Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures:

Segment Critical Systems:

- Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers.
- Use VLANs, firewalls, or routers to enforce logical separation.

Implement DMZ for Public-Facing Services:

- Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems.
- Apply strict firewall rules to filter traffic between the DMZ and internal networks.

Use Cloud-Based Segmentation:

- In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules.
- Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments.

Apply Microsegmentation for Workloads:

- Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement.

Restrict Traffic with ACLs and Firewalls:

- Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies.
- Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic.

Monitor and Audit Segmented Networks:

- Regularly review firewall rules, ACLs, and segmentation policies.
- Monitor network flows for anomalies to ensure segmentation is effective.

Test Segmentation Effectiveness:

- Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

## Techniques Mitigated
- T1021.001: Remote Desktop Protocol
- T1021.003: Distributed Component Object Model
- T1021.006: Windows Remote Management
- T1040: Network Sniffing
- T1046: Network Service Discovery
- T1048: Exfiltration Over Alternative Protocol
- T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1072: Software Deployment Tools
- T1095: Non-Application Layer Protocol
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1133: External Remote Services
- T1136: Create Account
- T1136.002: Domain Account
- T1136.003: Cloud Account
- T1190: Exploit Public-Facing Application
- T1199: Trusted Relationship
- T1210: Exploitation of Remote Services
- T1482: Domain Trust Discovery
- T1489: Service Stop
- T1552.007: Container API
- T1557: Adversary-in-the-Middle
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1563: Remote Service Session Hijacking
- T1563.002: RDP Hijacking
- T1565: Data Manipulation
- T1565.003: Runtime Data Manipulation
- T1571: Non-Standard Port
- T1602: Data from Configuration Repository
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump
- T1610: Deploy Container
- T1612: Build Image on Host
- T1613: Container and Resource Discovery
- T1669: Wi-Fi Networks
