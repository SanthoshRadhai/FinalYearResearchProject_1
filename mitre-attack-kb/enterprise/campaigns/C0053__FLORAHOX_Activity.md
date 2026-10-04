# C0053: FLORAHOX Activity

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0053  
**Aliases:** FLORAHOX Activity  

## Description
[FLORAHOX Activity](https://attack.mitre.org/campaigns/C0053) is conducted using a hybrid operational relay box (ORB) network, which combines two types of infrastructure: compromised devices and leased Virtual Private Servers (VPS). The compromised devices include end-of-life routers and IoT devices, while VPS space is commercially leased and managed by ORB network administrators. This hybrid ORB network allows adversaries to proxy and obscure malicious traffic, making the source of the traffic more difficult to trace.

The FLORAHOX ORB network has been leveraged by multiple cyber threat actors, including China-nexus actors like [ZIRCONIUM](https://attack.mitre.org/groups/G0128). These adversaries conduct espionage campaigns through [FLORAHOX Activity](https://attack.mitre.org/campaigns/C0053), relying on the ORB network's ability to funnel traffic through [Tor](https://attack.mitre.org/software/S0183) nodes, provisioned VPS servers, and compromised routers to obfuscate malicious traffic.(Citation: ORB Mandiant)
