# CWE-43: Path Equivalence: 'filename....' (Multiple Trailing Dot)

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/43.html  

## Description
The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Related Weaknesses
- ChildOf: CWE-42
- ChildOf: CWE-163

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Files or Directories, Modify Files or Directories
