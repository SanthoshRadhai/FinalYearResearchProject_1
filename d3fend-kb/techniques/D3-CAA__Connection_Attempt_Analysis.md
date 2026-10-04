# D3-CAA: Connection Attempt Analysis

**Synonym(s):** Network Scan Detection  
**Reference:** https://d3fend.mitre.org/technique/D3-CAA/  

## Definition
Analyzing failed connections in a network to detect unauthorized activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet Network Traffic
- **kb-reference:** Reference - Detecting network reconnaissance by tracking intranet dark-net communications - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Connection Attempt Analysis in multiple ways.

### Monitoring traffic to unallocated IP space
One approach looks for failed connection attempts against unallocated IP space. First, network traffic is captured to map out the network to identify network assets as well as unallocated IP space. The map is then used to determine if connection attempts are being made to the unallocated IP space.

### Monitoring for sequentially transmitted traffic
Another approach passively inspects network traffic with application protocol analyzers observing network activity characteristics such as volume of packets sent/ received, TCP session attributes, and connection information between hosts (start time, source/destination host, services, etc.). Then using pattern matching to identify traffic which appears to be probing for network hosts.

## Considerations

* Implementations that rely on analysis of unallocated IP address space increase in their complexity with network size and decentralized network infrastructure.
* Inventory of unallocated IP space should be continuously updated to mitigate the risk of false positives.
* IPv6 also introduces challenges including IPv6 traffic bypassing IPv4 specific protection systems (ex. firewalls and IDS) and complexity in managing both IPv6 and IPv4 addresses.
