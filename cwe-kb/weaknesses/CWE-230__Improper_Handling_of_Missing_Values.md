# CWE-230: Improper Handling of Missing Values

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/230.html  

## Description
The product does not handle or incorrectly handles when a parameter, field, or argument name is specified, but the associated value is missing, i.e. it is empty, blank, or null.

## Related Weaknesses
- ChildOf: CWE-229

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- This Android application has registered to handle a URL when sent an intent:
