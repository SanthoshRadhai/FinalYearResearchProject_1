# CAPEC-285: ICMP Echo Request Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/285.html  

## Description
An adversary sends out an ICMP Type 8 Echo Request, commonly known as a 'Ping', in order to determine if a target system is responsive. If the request is not blocked by a firewall or ACL, the target host will respond with an ICMP Type 0 Echo Reply datagram. This type of exchange is usually referred to as a 'Ping' due to the Ping utility present in almost all operating systems. Ping, as commonly implemented, allows a user to test for alive hosts, measure round-trip time, and measure the percentage of packet loss.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP type 8 query (Echo Request) to a remote target and receive an ICMP type 0 message (ICMP Echo Reply) in response. Any firewalls or access control lists between the sender and receiver must allow ICMP Type 8 and ICMP Type 0 messages in order for a ping operation to succeed.

## Skills Required
- [Low] The adversary needs to know certain linux commands for this type of attack.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Consider configuring firewall rules to block ICMP Echo requests and prevent replies. If not practical, monitor and consider action when a system has fast and a repeated pattern of requests that move incrementally through port numbers.

## Related Weaknesses (CWE)
- CWE-200
