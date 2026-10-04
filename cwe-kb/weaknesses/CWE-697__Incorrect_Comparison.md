# CWE-697: Incorrect Comparison

**Abstraction:** Pillar  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/697.html  

## Description
The product compares two entities in a security-relevant context, but the comparison is incorrect.

## Extended Description
This Pillar covers several possibilities: the comparison checks one factor incorrectly; the comparison should consider multiple factors, but it does not check at least one of those factors at all; the comparison checks the wrong factor.

## Common Consequences
- Scope: Other; Impact: Varies by Context — When the comparison is incorrect, it may lead to resultant weaknesses.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Consider an application in which Truck objects are defined to be the same if they have the same make, the same model, and were manufactured in the same year.
- This example defines a fixed username and password. The AuthenticateUser() function is intended to accept a username and a password from an untrusted user, and check to ensure that it matches the username and password. If the username and password match, AuthenticateUser() is intended to indicate that authentication succeeded.
