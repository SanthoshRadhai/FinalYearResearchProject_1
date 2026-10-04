# CAPEC-331: ICMP IP Total Length Field Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/331.html  

## Description
An adversary sends a UDP packet to a closed port on the target machine to solicit an IP Header's total length field value within the echoed 'Port Unreachable" error message. This type of behavior is useful for building a signature-base of operating system responses, particularly when error messages contain other types of information that is useful identifying specific operating system responses.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable."

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-204
