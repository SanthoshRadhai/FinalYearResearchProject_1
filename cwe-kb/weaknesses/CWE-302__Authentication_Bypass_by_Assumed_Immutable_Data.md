# CWE-302: Authentication Bypass by Assumed-Immutable Data

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/302.html  

## Description
The authentication scheme or implementation uses key data elements that are assumed to be immutable, but can be controlled or modified by the attacker.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-807

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design, Operation, Implementation] Implement proper protection for immutable data (e.g. environment variable, hidden form fields, etc.)

## Demonstrative Examples (summary)
- In the following example, an "authenticated" cookie is used to determine whether or not a user should be granted access to a system.
