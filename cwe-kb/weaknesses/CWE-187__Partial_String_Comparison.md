# CWE-187: Partial String Comparison

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/187.html  

## Description
The product performs a comparison that only examines a portion of a factor before determining whether there is a match, such as a substring, leading to resultant weaknesses.

## Extended Description
For example, an attacker might succeed in authentication by providing a small password that matches the associated portion of the larger, correct password.

## Related Weaknesses
- ChildOf: CWE-1023

## Common Consequences
- Scope: Integrity, Access Control; Impact: Alter Execution Logic, Bypass Protection Mechanism

## Potential Mitigations
- [Testing] Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

## Demonstrative Examples (summary)
- This example defines a fixed username and password. The AuthenticateUser() function is intended to accept a username and a password from an untrusted user, and check to ensure that it matches the username and password. If the username and password match, AuthenticateUser() is intended to indicate that authentication succeeded.
