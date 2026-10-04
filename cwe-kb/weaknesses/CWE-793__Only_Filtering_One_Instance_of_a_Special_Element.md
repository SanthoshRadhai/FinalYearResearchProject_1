# CWE-793: Only Filtering One Instance of a Special Element

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/793.html  

## Description
The product receives data from an upstream component, but only filters a single instance of a special element before sending it to a downstream component.

## Extended Description
Incomplete filtering of this nature may be location-dependent, as in only the first or last element is filtered.

## Related Weaknesses
- ChildOf: CWE-792

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter "../" from the input. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
