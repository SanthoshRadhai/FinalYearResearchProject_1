# CWE-797: Only Filtering Special Elements at an Absolute Position

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/797.html  

## Description
The product receives data from an upstream component, but only accounts for special elements at an absolute position (e.g. "byte number 10"), thereby missing remaining special elements that may exist before sending it to a downstream component.

## Related Weaknesses
- ChildOf: CWE-795

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a substring function to filter a 3-character "../" element located at the 0-index position of the input string. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
