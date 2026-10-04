# M0814: Static Network Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0814  

## Description
Configure hosts and devices to use static network configurations when possible, protocols that require dynamic discovery/addressing (e.g., ARP, DHCP, DNS) can be used to manipulate network message forwarding and enable various AiTM attacks. This mitigation may not always be usable due to limited device features or challenges introduced with different network configurations.

## Techniques Mitigated
- T0830: Adversary-in-the-Middle
- T0842: Network Sniffing
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0878: Alarm Suppression
- T0888: Remote System Information Discovery
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message
