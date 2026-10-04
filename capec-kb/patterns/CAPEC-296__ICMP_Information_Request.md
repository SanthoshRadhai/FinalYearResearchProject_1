# CAPEC-296: ICMP Information Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/296.html  

## Description
An adversary sends an ICMP Information Request to a host to determine if it will respond to this deprecated mechanism. ICMP Information Requests are a deprecated message type. Information Requests were originally used for diskless machines to automatically obtain their network configuration, but this message type has been superseded by more robust protocol implementations like DHCP.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP Type 15 Information Request and receive an ICMP Type 16 Information Reply in response.

## Skills Required
- [Low] The adversary needs to know certain linux commands for this type of attack.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200
