# CWE-75: Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/75.html  

## Description
The product does not adequately filter user-controlled input for special elements with control implications.

## Related Weaknesses
- ChildOf: CWE-74

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Application Data, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Requirements] Programming languages and supporting technologies might be chosen which are not subject to these issues.
- [Implementation] Utilize an appropriate mix of allowlist and denylist parsing to filter special element syntax from all input.
