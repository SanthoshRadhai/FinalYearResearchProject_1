# CAPEC-299: TCP SYN Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/299.html  

## Description
An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN "synchronize" packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in response. When a port is closed, RFC 793 behavior is to respond with a RST "reset" packet. This behavior can be used to 'ping' a target to see if it is alive by sending a TCP SYN packet to a port and then looking for a RST or an ACK packet in response.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send a TCP SYN packet to a remote target. Depending upon the operating system, the ability to craft SYN packets may require elevated privileges.

## Skills Required
- [Low] The adversary needs to know how to craft and send protocol commands from the command line or within a tool.

## Resources Required
- SYN pings can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
