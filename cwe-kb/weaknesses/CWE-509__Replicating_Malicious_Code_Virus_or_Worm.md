# CWE-509: Replicating Malicious Code (Virus or Worm)

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/509.html  

## Description
Replicating malicious code, including viruses and worms, will attempt to attack other systems once it has successfully compromised the target system or the product.

## Related Weaknesses
- ChildOf: CWE-507

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands

## Potential Mitigations
- [Operation] Antivirus software scans for viruses or worms.
- [Installation] Always verify the integrity of the software that is being installed.
