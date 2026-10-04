# CAPEC-322: TCP (ISN) Greatest Common Divisor Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/322.html  

## Description
This OS fingerprinting probe sends a number of TCP SYN packets to an open port of a remote machine. The Initial Sequence Number (ISN) in each of the SYN/ACK response packets is analyzed to determine the smallest number that the target host uses when incrementing sequence numbers. This information can be useful for identifying an operating system because particular operating systems and versions increment sequence numbers using different values. The result of the analysis is then compared against a database of OS behaviors to determine the OS type and/or version.

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
