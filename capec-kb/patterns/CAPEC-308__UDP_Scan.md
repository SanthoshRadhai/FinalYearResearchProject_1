# CAPEC-308: UDP Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/308.html  

## Description
An adversary engages in UDP scanning to gather information about UDP port status on the target system. UDP scanning methods involve sending a UDP datagram to the target port and looking for evidence that the port is closed. Open UDP ports usually do not respond to UDP datagrams as there is no stateful mechanism within the protocol that requires building or establishing a session. Responses to UDP datagrams are therefore application specific and cannot be relied upon as a method of detecting an open port. UDP scanning relies heavily upon ICMP diagnostic messages in order to determine the status of a remote port.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The ability to send UDP datagrams to a host and receive ICMP error messages from that host. In cases where particular types of ICMP messaging is disallowed, the reliability of UDP scanning drops off sharply.

## Resources Required
- The ability to craft custom UDP Packets for use during network reconnaissance. This can be accomplished via the use of a port scanner, or via socket manipulation in a programming or scripting language. Packet injection tools are also useful. It is also necessary to trap ICMP diagnostic messages during this process. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Firewalls or ACLs which block egress ICMP error types effectively prevent UDP scans from returning any useful information.
- UDP scanning is complicated by rate limiting mechanisms governing ICMP error messages.

## Related Weaknesses (CWE)
- CWE-200
