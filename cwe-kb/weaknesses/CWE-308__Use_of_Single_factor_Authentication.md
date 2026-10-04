# CWE-308: Use of Single-factor Authentication

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/308.html  

## Description
The product uses an authentication algorithm that uses a single factor (e.g., a password) in a security context that should require more than one factor.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-654
- PeerOf: CWE-309

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — If the secret in a single-factor authentication scheme gets compromised, full authentication is possible.

## Potential Mitigations
- [Architecture and Design] Use multiple independent authentication schemes, which ensures that -- if one of the methods is compromised -- the system itself is still likely safe from compromise. For this reason, if multiple schemes are possible, they should be implemented and required -- especially if they are easy to use.

## Demonstrative Examples (summary)
- In both of these examples, a user is logged in if their given password matches a stored password:
