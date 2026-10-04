# CWE-42: Path Equivalence: 'filename.' (Trailing Dot)

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/42.html  

## Description
The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Related Weaknesses
- ChildOf: CWE-41
- ChildOf: CWE-162

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism
