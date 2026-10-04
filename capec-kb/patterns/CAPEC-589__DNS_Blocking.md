# CAPEC-589: DNS Blocking

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/589.html  

## Description
An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user even if the IP address is changed.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Hard Coded Alternate DNS server in applications
- Avoid dependence on DNS
- Include "hosts file"/IP address in the application.
- Ensure best practices with respect to communications channel protections.
- Use a .onion domain with Tor support

## Related Weaknesses (CWE)
- CWE-300
