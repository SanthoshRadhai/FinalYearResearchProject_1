# CAPEC-317: IP ID Sequencing Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/317.html  

## Description
This OS fingerprinting probe analyzes the IP 'ID' field sequence number generation algorithm of a remote host. Operating systems generate IP 'ID' numbers differently, allowing an attacker to identify the operating system of the host by examining how is assigns ID numbers when generating response packets. RFC 791 does not specify how ID numbers are chosen or their ranges, so ID sequence generation differs from implementation to implementation. There are two kinds of IP 'ID' sequence number analysis - IP 'ID' Sequencing: analyzing the IP 'ID' sequence generation algorithm for one protocol used by a host and Shared IP 'ID' Sequencing: analyzing the packet ordering via IP 'ID' values spanning multiple protocols, such as between ICMP and TCP.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
