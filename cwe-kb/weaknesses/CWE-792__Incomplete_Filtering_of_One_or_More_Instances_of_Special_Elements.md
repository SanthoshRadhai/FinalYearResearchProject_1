# CWE-792: Incomplete Filtering of One or More Instances of Special Elements

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/792.html  

## Description
The product receives data from an upstream component, but does not completely filter one or more instances of special elements before sending it to a downstream component.

## Extended Description
Incomplete filtering of this nature involves either: only filtering a single instance of a special element when more exist, or not filtering all instances or all elements where multiple special elements exist.

## Related Weaknesses
- ChildOf: CWE-791

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter "../" from the input. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
