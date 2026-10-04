# CWE-507: Trojan Horse

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/507.html  

## Description
The product appears to contain benign or useful functionality, but it also contains code that is hidden from normal operation that violates the intended security policy of the user or the system administrator.

## Related Weaknesses
- ChildOf: CWE-506

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands

## Potential Mitigations
- [Operation] Most antivirus software scans for Trojan Horses.
- [Installation] Verify the integrity of the product that is being installed.
