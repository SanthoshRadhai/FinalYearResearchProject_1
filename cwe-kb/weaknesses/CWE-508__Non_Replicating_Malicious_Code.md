# CWE-508: Non-Replicating Malicious Code

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/508.html  

## Description
Non-replicating malicious code only resides on the target system or product that is attacked; it does not attempt to spread to other systems.

## Related Weaknesses
- ChildOf: CWE-507

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Code or Commands

## Potential Mitigations
- [Operation] Antivirus software can help mitigate known malicious code.
- [Installation] Verify the integrity of the software that is being installed.
