# CWE-791: Incomplete Filtering of Special Elements

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/791.html  

## Description
The product receives data from an upstream component, but does not completely filter special elements before sending it to a downstream component.

## Related Weaknesses
- ChildOf: CWE-790

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter "../" from the input. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
