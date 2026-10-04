# D3-NTCD: Network Traffic Community Deviation

**Reference:** https://d3fend.mitre.org/technique/D3-NTCD/  

## Definition
Establishing baseline communities of network hosts and identifying statistically divergent inter-community communication.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - System for implementing threat detection using daily network traffic community outliers - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Hosts/users within a computer network are analyzed to identify communities of hosts which frequently communicate. Future communications between communities that don't usually communicate can then be detected.  For example, if a community of hosts that communicate in support of a company's finance division suddenly starts to access the code server usually accessed only by engineers, this may indicate unauthorized activity.

## Considerations
* Potential for false positives in very dynamic network environments.
* Attackers that move low and slow may not differentiate their behavior enough to trigger an alert.
