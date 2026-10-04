# CWE-424: Improper Protection of Alternate Path

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/424.html  

## Description
The product does not sufficiently protect all possible paths that a user can take to access restricted functionality or resources.

## Related Weaknesses
- ChildOf: CWE-693
- ChildOf: CWE-638

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design] Deploy different layers of protection to implement security in depth.
