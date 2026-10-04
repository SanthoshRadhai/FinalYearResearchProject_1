# CWE-1254: Incorrect Comparison Logic Granularity

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1254.html  

## Description
The product's comparison logic is performed over a series of steps rather than across the entire string in one operation. If there is a comparison logic failure on one of these steps, the operation may be vulnerable to a timing attack that can result in the interception of the process for nefarious purposes.

## Extended Description
Comparison logic is used to compare a variety of objects including passwords, Message Authentication Codes (MACs), and responses to verification challenges. When comparison logic is implemented at a finer granularity (e.g., byte-by-byte comparison) and breaks in the case of a comparison failure, an attacker can exploit this implementation to identify when exactly the failure occurred. With multiple attempts, the attacker may be able to guesses the correct password/response to challenge and elevate their privileges.

## Related Weaknesses
- ChildOf: CWE-208
- ChildOf: CWE-697

## Common Consequences
- Scope: Confidentiality, Authorization; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] The hardware designer should ensure that comparison logic is implemented so as to compare in one operation instead in smaller chunks.
