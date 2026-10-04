# CAPEC-491: Quadratic Data Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/491.html  

## Description
An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity and using it multiple times in a single entity substitution. CAPEC-197 is a similar attack pattern, but it is easier to discover and defend against. This attack pattern does not perform multi-level substitution and therefore does not obviously appear to consume extensive resources.

## Related Attack Patterns
- ChildOf: CAPEC-230

## Prerequisites
- This type of attack requires a server that accepts serialization data which supports substitution and parses the data.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related Weaknesses (CWE)
- CWE-770
