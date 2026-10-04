# CAPEC-298: UDP Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/298.html  

## Description
An adversary sends a UDP datagram to the remote host to determine if the host is alive. If a UDP datagram is sent to an open UDP port there is very often no response, so a typical strategy for using a UDP ping is to send the datagram to a random high port on the target. The goal is to solicit an 'ICMP port unreachable' message from the target, indicating that the host is alive. UDP pings are useful because some firewalls are not configured to block UDP datagrams sent to strange or typically unused ports, like ports in the 65K range. Additionally, while some firewalls may filter incoming ICMP, weaknesses in firewall rule-sets may allow certain types of ICMP (host unreachable, port unreachable) which are useful for UDP ping attempts.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The adversary requires the ability to send a UDP datagram to a remote host and receive a response.
- The adversary requires the ability to craft custom UDP Packets for use during network reconnaissance.
- The target's firewall must not be configured to block egress ICMP messages.

## Resources Required
- UDP pings can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Configure your firewall to block egress ICMP messages.

## Related Weaknesses (CWE)
- CWE-200
