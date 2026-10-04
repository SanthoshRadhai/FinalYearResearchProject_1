# CWE-1023: Incomplete Comparison with Missing Factors

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1023.html  

## Description
The product performs a comparison between entities that must consider multiple factors or characteristics of each entity, but the comparison does not include one or more of these factors.

## Related Weaknesses
- ChildOf: CWE-697

## Common Consequences
- Scope: Integrity, Access Control; Impact: Alter Execution Logic, Bypass Protection Mechanism — An incomplete comparison can lead to resultant weaknesses, e.g., by operating on the wrong object or making a security decision without considering a required factor.

## Detection Methods
- [Manual Static Analysis] Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

## Demonstrative Examples (summary)
- Consider an application in which Truck objects are defined to be the same if they have the same make, the same model, and were manufactured in the same year.
- This example defines a fixed username and password. The AuthenticateUser() function is intended to accept a username and a password from an untrusted user, and check to ensure that it matches the username and password. If the username and password match, AuthenticateUser() is intended to indicate that authentication succeeded.
