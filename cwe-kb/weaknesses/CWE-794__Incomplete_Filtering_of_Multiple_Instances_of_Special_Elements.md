# CWE-794: Incomplete Filtering of Multiple Instances of Special Elements

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/794.html  

## Description
The product receives data from an upstream component, but does not filter all instances of a special element before sending it to a downstream component.

## Extended Description
Incomplete filtering of this nature may be applied to: sequential elements (special elements that appear next to each other) or non-sequential elements (special elements that appear multiple times in different locations).

## Related Weaknesses
- ChildOf: CWE-792

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter "../" from the input. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
