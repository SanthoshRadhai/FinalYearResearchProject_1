# CWE-795: Only Filtering Special Elements at a Specified Location

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/795.html  

## Description
The product receives data from an upstream component, but only accounts for special elements at a specified location, thereby missing remaining special elements that may exist before sending it to a downstream component.

## Extended Description
A filter might only account for instances of special elements when they occur: relative to a marker (e.g. "at the beginning/end of string; the second argument"), or at an absolute position (e.g. "byte number 10"). This may leave special elements in the data that did not match the filter position, but still may be dangerous.

## Related Weaknesses
- ChildOf: CWE-791

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Demonstrative Examples (summary)
- The following code takes untrusted input and uses a regular expression to filter a "../" element located at the beginning of the input string. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
- The following code takes untrusted input and uses a substring function to filter a 3-character "../" element located at the 0-index position of the input string. It then appends this result to the /home/user/ directory and attempts to read the file in the final resulting path.
