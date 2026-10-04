# CWE-97: Improper Neutralization of Server-Side Includes (SSI) Within a Web Page

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/97.html  

## Description
The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive.

## Related Weaknesses
- ChildOf: CWE-96

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands
