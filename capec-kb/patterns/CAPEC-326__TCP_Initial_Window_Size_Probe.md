# CAPEC-326: TCP Initial Window Size Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/326.html  

## Description
This OS fingerprinting probe checks the initial TCP Window size. TCP stacks limit the range of sequence numbers allowable within a session to maintain the "connected" state within TCP protocol logic. The initial window size specifies a range of acceptable sequence numbers that will qualify as a response to an ACK packet within a session. Various operating systems use different Initial window sizes. The initial window size can be sampled by establishing an ordinary TCP connection.

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
