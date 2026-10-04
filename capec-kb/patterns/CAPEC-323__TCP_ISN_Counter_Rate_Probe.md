# CAPEC-323: TCP (ISN) Counter Rate Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/323.html  

## Description
This OS detection probe measures the average rate of initial sequence number increments during a period of time. Sequence numbers are incremented using a time-based algorithm and are susceptible to a timing analysis that can determine the number of increments per unit time. The result of this analysis is then compared against a database of operating systems and versions to determine likely operation system matches.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
