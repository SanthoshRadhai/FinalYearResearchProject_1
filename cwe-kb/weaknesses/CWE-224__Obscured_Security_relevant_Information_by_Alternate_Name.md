# CWE-224: Obscured Security-relevant Information by Alternate Name

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/224.html  

## Description
The product records security-relevant information according to an alternate name of the affected entity, instead of the canonical name.

## Related Weaknesses
- ChildOf: CWE-221

## Common Consequences
- Scope: Non-Repudiation, Access Control; Impact: Hide Activities, Gain Privileges or Assume Identity

## Demonstrative Examples (summary)
- This code prints the contents of a file if a user has permission.
