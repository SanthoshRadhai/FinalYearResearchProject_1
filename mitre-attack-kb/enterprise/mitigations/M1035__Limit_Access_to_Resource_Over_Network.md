# M1035: Limit Access to Resource Over Network

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1035  

## Description
Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures:

Audit and Restrict Access:

- Regularly audit permissions for file shares, network services, and remote access tools.
- Remove unnecessary access and enforce least privilege principles for users and services.
- Use Active Directory and IAM tools to restrict access based on roles and attributes.

Deploy Secure Remote Access Solutions:

- Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections.
- Configure access controls to restrict connections based on time, device, and user identity.
- Enforce MFA for all remote access mechanisms.

Disable Unnecessary Services:

- Identify running services using tools like netstat (Windows/Linux) or Nmap.
- Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface.
- Use firewall rules to block traffic on unused ports and protocols.

Network Segmentation and Isolation:

- Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access.
- Restrict communication between subnets to prevent lateral movement.

Monitor and Log Access:

- Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools.
- Enable auditing and logging for successful and failed attempts to access restricted resources.

*Tools for Implementation*

File Share Management:

- Microsoft Active Directory Group Policies
- Samba (Linux/Unix file share management)
- AccessEnum (Windows access auditing tool)

Secure Remote Access:

- Microsoft Remote Desktop Gateway
- Apache Guacamole (open-source RDP/VNC gateway)
- Zero Trust solutions: Tailscale, Cloudflare Zero Trust

Service and Protocol Hardening:

- Nmap or Nessus for network service discovery
- Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols
- iptables or firewalld (Linux) for blocking unnecessary traffic

Network Segmentation:

- pfSense for open-source network isolation

## Techniques Mitigated
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.002: SMB/Windows Admin Shares
- T1133: External Remote Services
- T1190: Exploit Public-Facing Application
- T1200: Hardware Additions
- T1542: Pre-OS Boot
- T1542.005: TFTP Boot
- T1546.008: Accessibility Features
- T1552: Unsecured Credentials
- T1552.005: Cloud Instance Metadata API
- T1552.007: Container API
- T1557: Adversary-in-the-Middle
- T1557.002: ARP Cache Poisoning
- T1563.002: RDP Hijacking
- T1609: Container Administration Command
- T1610: Deploy Container
- T1612: Build Image on Host
- T1613: Container and Resource Discovery
