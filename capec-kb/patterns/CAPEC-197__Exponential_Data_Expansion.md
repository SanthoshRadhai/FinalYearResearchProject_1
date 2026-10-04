# CAPEC-197: Exponential Data Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/197.html  

## Description
An adversary submits data to a target application which contains nested exponential data expansion to produce excessively large output. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. However, this capability can be abused to create excessive demands on a processor's CPU and memory. A small number of nested expansions can result in an exponential growth in demands on memory.

## Related Attack Patterns
- ChildOf: CAPEC-230

## Prerequisites
- This type of attack requires that the target must receive input but either fail to provide an upper limit for entity expansion or provide a limit that is so large that it does not preclude significant resource consumption.

## Skills Required
- [Low] Ability to craft nested data expansion messages.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related Weaknesses (CWE)
- CWE-770
- CWE-776
