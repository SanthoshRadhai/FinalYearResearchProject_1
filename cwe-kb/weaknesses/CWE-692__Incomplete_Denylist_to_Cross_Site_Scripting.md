# CWE-692: Incomplete Denylist to Cross-Site Scripting

**Abstraction:** Compound  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/692.html  

## Description
The product uses a denylist-based protection mechanism to defend against XSS attacks, but the denylist is incomplete, allowing XSS variants to succeed.

## Extended Description
While XSS might seem simple to prevent, web browsers vary so widely in how they parse web pages, that a denylist cannot keep track of all the variations. The "XSS Cheat Sheet" [REF-714] contains a large number of attacks that are intended to bypass incomplete denylists.

## Related Weaknesses
- StartsWith: CWE-184
- ChildOf: CWE-184

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands
