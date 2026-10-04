# CWE-1331: Improper Isolation of Shared Resources in Network On Chip (NoC)

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1331.html  

## Description
The Network On Chip (NoC) does not isolate or incorrectly isolates its on-chip-fabric and internal resources such that they are shared between trusted and untrusted agents, creating timing channels.

## Extended Description
Typically, network on chips (NoC) have many internal resources that are shared between packets from different trust domains. These resources include internal buffers, crossbars and switches, individual ports, and channels. The sharing of resources causes contention and introduces interference between differently trusted domains, which poses a security threat via a timing channel, allowing attackers to infer data that belongs to a trusted agent. This may also result in introducing network interference, resulting in degraded throughput and latency.

## Related Weaknesses
- ChildOf: CWE-653
- ChildOf: CWE-668
- PeerOf: CWE-1189

## Common Consequences
- Scope: Confidentiality, Availability; Impact: DoS: Resource Consumption (Other), Varies by Context, Other — Attackers may infer data that belongs to a trusted agent. The methods used to perform this attack may result in noticeably increased resource consumption.

## Potential Mitigations
- [Architecture and Design, Implementation] Implement priority-based arbitration inside the NoC and have dedicated buffers or virtual channels for routing secret data from trusted agents.

## Detection Methods
- [Manual Analysis] Providing marker flags to send through the interfaces coupled with examination of which users are able to read or manipulate the flags will help verify that the proper isolation has been achieved and is effective.

## Demonstrative Examples (summary)
- Consider a NoC that implements a one-dimensional mesh network with four nodes. This supports two flows: Flow A from node 0 to node 3 (via node 1 and node 2) and Flow B from node 1 to node 2. Flows A and B share a common link between Node 1 and Node 2. Only one flow can use the link in each cycle.
