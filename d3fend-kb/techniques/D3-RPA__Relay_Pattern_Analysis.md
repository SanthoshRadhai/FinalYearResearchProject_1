# D3-RPA: Relay Pattern Analysis

**Synonym(s):** Relay Network Detection  
**Reference:** https://d3fend.mitre.org/technique/D3-RPA/  

## Definition
The detection of an internal host relaying traffic between the internal network and the external network.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Outbound Internet Network Traffic
- **kb-reference:** Reference - Malicious relay detection on networks - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
A relay may use a variety of proxying, forwarding, or routing technologies to bridge a protected network with an external network. A defensive analytic to detect a relay network may compare the network sessions among multiple hosts. Hosts which have nearly similar network statistics may be part of a relay network. The statistics may include number of bytes sent to and from, time of session initiation, packet size, or packet arrival time data.

## Considerations

Complex intranet VPNs or routing encapsulation may affect the detection analytics.  In addition, unwanted packets might not be forwarded, and additional packets may be added at the relay, further complicating detection.
