# D3-BDI: Broadcast Domain Isolation

**Synonym(s):** Network Segmentation  
**Reference:** https://d3fend.mitre.org/technique/D3-BDI/  

## Definition
Broadcast isolation restricts the number of computers a host can contact on their LAN.

## Parent Class(es)
- Network Isolation

## Relationships
- **filters:** Local Area Network Traffic
- **kb-reference:** Reference - Broadcast isolation and level 3 network switch - Hewlett Packard Enterprise Development LP
- **kb-reference:** Reference - Private virtual local area network isolation - Cisco Technology Inc

## Knowledge Base Article
## How it works
Software Defined Networking, or other network encapsulation technologies intercept host broadcast traffic then route it to a specified destination per a configured policy.

This can be implemented within hypervisors, networking hardware (WAPs, switches, routers), or virtual hardware.

## Considerations
This technique is highly dependent on network infrastructure and networking requirements.
