# CWE-1174: ASP.NET Misconfiguration: Improper Model Validation

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1174.html  

## Description
The ASP.NET application does not use, or incorrectly uses, the model validation framework.

## Related Weaknesses
- ChildOf: CWE-1173

## Common Consequences
- Scope: Integrity; Impact: Unexpected State — Unchecked input leads to cross-site scripting, process control, and SQL injection vulnerabilities, among others.
