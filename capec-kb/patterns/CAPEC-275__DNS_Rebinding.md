# CAPEC-275: DNS Rebinding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/275.html  

## Description
An adversary serves content whose IP address is resolved by a DNS server that the adversary controls. After initial contact by a web browser (or similar client), the adversary changes the IP address to which its name resolves, to an address within the target organization that is not publicly accessible. This allows the web browser to examine this internal address on behalf of the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- The target browser must access content server from the adversary controlled DNS name. Web advertisements are often used for this purpose. The target browser must honor the TTL value returned by the adversary and re-resolve the adversary's DNS name after initial contact.

## Skills Required
- [Medium] Setup DNS server and the adversary's web server. Write a malicious script to allow the victim to connect to the web server.

## Resources Required
- The adversary must serve some web content that a victim accesses initially. This content must include executable content that queries the adversary's DNS name (to provide the second DNS resolution) and then performs the follow-on attack against the internal system. The adversary also requires a customized DNS server that serves an IP address for their registered DNS name, but which resolves subsequent requests by a single client to addresses internal to that client's network.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: IP Pinning causes browsers to record the IP address to which a given name resolves and continue using this address regardless of the TTL set in the DNS response. Unfortunately, this is incompatible with the design of some legitimate sites.
- Implementation: Reject HTTP request with a malicious Host header.
- Implementation: Employ DNS resolvers that prevent external names from resolving to internal addresses.

## Related Weaknesses (CWE)
- CWE-350
