# CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/349.html  

## Description
The product, when processing trusted data, accepts any untrusted data that is also included with the trusted data, treating the untrusted data as if it were trusted.

## Related Weaknesses
- ChildOf: CWE-345

## Common Consequences
- Scope: Access Control, Integrity; Impact: Bypass Protection Mechanism, Modify Application Data — An attacker could package untrusted data with trusted data to bypass protection mechanisms to gain access to and possibly modify sensitive data.
