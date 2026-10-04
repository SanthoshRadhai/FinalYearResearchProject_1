# CAPEC-330: ICMP Error Message Echoing Integrity Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/330.html  

## Description
An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the integrity of data returned or "Quoted" from the originating request that generated the error message.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable..

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
