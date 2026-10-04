# CWE-232: Improper Handling of Undefined Values

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/232.html  

## Description
The product does not handle or incorrectly handles when a value is not defined or supported for the associated parameter, field, or argument name.

## Related Weaknesses
- ChildOf: CWE-229

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- In this example, an address parameter is read and trimmed of whitespace.
