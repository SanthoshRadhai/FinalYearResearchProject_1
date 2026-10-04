# CWE-222: Truncation of Security-relevant Information

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/222.html  

## Description
The product truncates the display, recording, or processing of security-relevant information in a way that can obscure the source or nature of an attack.

## Related Weaknesses
- ChildOf: CWE-221

## Common Consequences
- Scope: Non-Repudiation; Impact: Hide Activities — The source of an attack will be difficult or impossible to determine. This can allow attacks to the system to continue without notice.
