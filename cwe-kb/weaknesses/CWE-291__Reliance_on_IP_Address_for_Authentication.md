# CWE-291: Reliance on IP Address for Authentication

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/291.html  

## Description
The product uses an IP address for authentication.

## Extended Description
IP addresses can be easily spoofed. Attackers can forge the source IP address of the packets they send, but response packets will return to the forged IP address. To see the response packets, the attacker has to sniff the traffic between the victim machine and the forged IP address. In order to accomplish the required sniffing, attackers typically attempt to locate themselves on the same subnet as the victim machine. Attackers may be able to circumvent this requirement by using source routing, but source routing is disabled across much of the Internet today. In summary, IP address verification can be a useful part of an authentication scheme, but it should not be the single factor required for authentication.

## Related Weaknesses
- ChildOf: CWE-290
- ChildOf: CWE-923

## Common Consequences
- Scope: Access Control, Non-Repudiation; Impact: Hide Activities, Gain Privileges or Assume Identity — Malicious users can fake authentication information, impersonating any IP address.

## Potential Mitigations
- [Architecture and Design] Use other means of identity verification that cannot be simply spoofed. Possibilities include a username/password or certificate.

## Demonstrative Examples (summary)
- Both of these examples check if a request is from a trusted address before responding to the request.
