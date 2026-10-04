# CAPEC-294: ICMP Address Mask Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/294.html  

## Description
An adversary sends an ICMP Type 17 Address Mask Request to gather information about a target's networking configuration. ICMP Address Mask Requests are defined by RFC-950, "Internet Standard Subnetting Procedure." An Address Mask Request is an ICMP type 17 message that triggers a remote system to respond with a list of its related subnets, as well as its default gateway and broadcast address via an ICMP type 18 Address Mask Reply datagram. Gathering this type of information helps the adversary plan router-based attacks as well as denial-of-service attacks against the broadcast address.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP type 17 query (Address Mask Request) to a remote target and receive an ICMP type 18 message (ICMP Address Mask Reply) in response. Generally, modern operating systems will ignore ICMP type 17 messages, however, routers will commonly respond to this request.

## Resources Required
- The ability to send custom ICMP queries. This can be accomplished via the use of various scanners or utilities.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200
