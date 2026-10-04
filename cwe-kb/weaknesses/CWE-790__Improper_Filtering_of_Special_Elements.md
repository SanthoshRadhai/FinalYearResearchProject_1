# CWE-790: Improper Filtering of Special Elements

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/790.html  

## Description
The product receives data from an upstream component, but does not filter or incorrectly filters special elements before sending it to a downstream component.

## Related Weaknesses
- ChildOf: CWE-138

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter "../" from the input. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
