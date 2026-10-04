# CAPEC-324: TCP (ISN) Sequence Predictability Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/324.html  

## Description
This type of operating system probe attempts to determine an estimate for how predictable the sequence number generation algorithm is for a remote host. Statistical techniques, such as standard deviation, can be used to determine how predictable the sequence number generation is for a system. This result can then be compared to a database of operating system behaviors to determine a likely match for operating system and version.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
