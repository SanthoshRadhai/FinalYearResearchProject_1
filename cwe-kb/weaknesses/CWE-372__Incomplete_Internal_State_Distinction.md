# CWE-372: Incomplete Internal State Distinction

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/372.html  

## Description
The product does not properly determine which state it is in, causing it to assume it is in state X when in fact it is in state Y, causing it to perform incorrect operations in a security-relevant manner.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Integrity, Other; Impact: Varies by Context, Unexpected State
