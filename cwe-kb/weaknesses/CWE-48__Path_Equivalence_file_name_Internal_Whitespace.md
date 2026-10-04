# CWE-48: Path Equivalence: 'file name' (Internal Whitespace)

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/48.html  

## Description
The product accepts path input in the form of internal space ('file(SPACE)name') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Related Weaknesses
- ChildOf: CWE-41

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Files or Directories, Modify Files or Directories
