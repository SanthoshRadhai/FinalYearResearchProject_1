# CWE-223: Omission of Security-relevant Information

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/223.html  

## Description
The product does not record or display information that would be important for identifying the source or nature of an attack, or determining if an action is safe.

## Related Weaknesses
- ChildOf: CWE-221

## Common Consequences
- Scope: Non-Repudiation; Impact: Hide Activities — The source of an attack will be difficult or impossible to determine. This can allow attacks to the system to continue without notice.

## Demonstrative Examples (summary)
- This code logs suspicious multiple login attempts.
- This code prints the contents of a file if a user has permission.
