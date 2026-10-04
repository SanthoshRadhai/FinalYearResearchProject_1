# D3-ISVA: Inbound Session Volume Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ISVA/  

## Definition
Analyzing inbound network session or connection attempt volume.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Inbound Internet Network Traffic
- **kb-reference:** Reference - Detecting DDoS Attack Using Snort
- **kb-reference:** Reference - Identifying a denial-of-service attack in a cloud-based proxy service - Cloudfare Inc.
- **kb-reference:** Reference - Method and system for UDP flood attack detection - Riorey LLC
- **kb-reference:** Reference - Protecting against distributed denial of service attacks - Cisco Technology Inc.
- **kb-reference:** Reference - Protecting against distributed network flood attacks - Juniper Networks Inc.

## Knowledge Base Article
## How it works
Network appliances are configured to alert on certain packets that typically are involved in DoS attacks. Typical packets include ICMP packets and SYN requests that are commonly used to flood networks. A sampling period is used to define a time window in which collected counts of the identified packets can be measured. If the collected number of packets exceeds a predefined limit then an alert is generated.

## Considerations
Scalability as volume of attacks increase; single servers may not have the memory and storage resources to handle high volumes of network traffic.
