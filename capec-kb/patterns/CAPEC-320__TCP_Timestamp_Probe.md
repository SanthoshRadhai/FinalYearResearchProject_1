# CAPEC-320: TCP Timestamp Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/320.html  

## Description
This OS fingerprinting probe examines the remote server's implementation of TCP timestamps. Not all operating systems implement timestamps within the TCP header, but when timestamps are used then this provides the attacker with a means to guess the operating system of the target. The attacker begins by probing any active TCP service in order to get response which contains a TCP timestamp. Different Operating systems update the timestamp value using different intervals. This type of analysis is most accurate when multiple timestamp responses are received and then analyzed. TCP timestamps can be found in the TCP Options field of the TCP header.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.The target OS must support the TCP timestamp option in order to obtain a fingerprint.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Related Weaknesses (CWE)
- CWE-200
