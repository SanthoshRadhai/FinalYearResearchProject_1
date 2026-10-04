# CWE-221: Information Loss or Omission

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/221.html  

## Description
The product does not record, or improperly records, security-relevant information that leads to an incorrect decision or hampers later analysis.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Non-Repudiation; Impact: Hide Activities

## Demonstrative Examples (summary)
- This code logs suspicious multiple login attempts.
