# CWE-531: Inclusion of Sensitive Information in Test Code

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/531.html  

## Description
Accessible test applications can pose a variety of security risks. Since developers or administrators rarely consider that someone besides themselves would even know about the existence of these applications, it is common for them to contain sensitive information or functions.

## Related Weaknesses
- ChildOf: CWE-540

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Distribution, Installation] Remove test code before deploying the application into production.

## Demonstrative Examples (summary)
- Examples of common issues with test applications include administrative functions, listings of usernames, passwords or session identifiers and information about the system, server or application configuration.
