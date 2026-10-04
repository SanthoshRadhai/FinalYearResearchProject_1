# CAPEC-313: Passive OS Fingerprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/313.html  

## Description
An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor network or client-server communication between nodes in order to identify operating systems based on observed behavior as compared to a database of known signatures or values. While passive OS fingerprinting is not usually as reliable as active methods, it is generally better able to evade detection.

## Related Attack Patterns
- ChildOf: CAPEC-224

## Prerequisites
- The ability to monitor network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any tool capable of monitoring network communications, like a packet sniffer (e.g., Wireshark)

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200
