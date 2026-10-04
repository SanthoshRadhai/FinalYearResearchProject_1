# CWE-290: Authentication Bypass by Spoofing

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/290.html  

## Description
This attack-focused weakness is caused by incorrectly implemented authentication schemes that are subject to spoofing attacks.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-287

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — This weakness can allow an attacker to access resources which are not otherwise accessible without proper authentication.

## Demonstrative Examples (summary)
- The following code authenticates users.
- Both of these examples check if a request is from a trusted address before responding to the request.
- The following code samples use a DNS lookup in order to decide whether or not an inbound request is from a trusted host. If an attacker can poison the DNS cache, they can gain trusted status.
