# CAPEC-481: Contradictory Destinations in Traffic Routing Schemes

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/481.html  

## Description
Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there are contradictory domain names provided it is possible to route traffic to an inappropriate destination. The technique, called Domain Fronting, involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. An alternative technique, called Domainless Fronting, is similar, but the SNI field is left blank.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- An adversary must be aware that their message will be routed using a CDN, and that both of the contradictory domains are served from that CDN.
- If the purpose of the Domain Fronting is to hide redirected C2 traffic, the C2 server must have been created in the CDN.

## Skills Required
- [Medium] The adversary must have some knowledge of how messages are routed.

## Consequences
- Scope: Confidentiality; Impact: Read Data, Modify Data

## Mitigations
- Monitor connections, checking headers in traffic for contradictory domain names, or empty domain names.

## Related Weaknesses (CWE)
- CWE-923
