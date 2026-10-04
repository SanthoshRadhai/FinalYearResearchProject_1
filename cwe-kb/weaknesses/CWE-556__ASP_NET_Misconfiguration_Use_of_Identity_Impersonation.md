# CWE-556: ASP.NET Misconfiguration: Use of Identity Impersonation

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/556.html  

## Description
Configuring an ASP.NET application to run with impersonated credentials may give the application unnecessary privileges.

## Extended Description
The use of impersonated credentials allows an ASP.NET application to run with either the privileges of the client on whose behalf it is executing or with arbitrary privileges granted in its configuration.

## Related Weaknesses
- ChildOf: CWE-266

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design] Use the least privilege principle.
