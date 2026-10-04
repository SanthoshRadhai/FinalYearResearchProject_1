# CAPEC-309: Network Topology Mapping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/309.html  

## Description
An adversary engages in scanning activities to map network nodes, hosts, devices, and routes. Adversaries usually perform this type of network reconnaissance during the early stages of attack against an external network. Many types of scanning utilities are typically employed, including ICMP tools, network mappers, port scanners, and route testing utilities such as traceroute.

## Related Attack Patterns
- ChildOf: CAPEC-169
- CanPrecede: CAPEC-664

## Prerequisites
- None

## Resources Required
- Probing requires the ability to interactively send and receive data from a target, whereas passive listening requires a sufficient understanding of the protocol to analyze a preexisting channel of communication.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200
