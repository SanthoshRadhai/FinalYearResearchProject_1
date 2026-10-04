# CWE-72: Improper Handling of Apple HFS+ Alternate Data Stream Path

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/72.html  

## Description
The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.

## Extended Description
If the product chooses actions to take based on the file name, then if an attacker provides the data or resource fork, the product may take unexpected actions. Further, if the product intends to restrict access to a file, then an attacker might still be able to bypass intended access restrictions by requesting the data or resource fork for that file.

## Related Weaknesses
- ChildOf: CWE-66

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Files or Directories, Modify Files or Directories

## Demonstrative Examples (summary)
- Consider a web server that uses the Apple HFS+ file system. It interprets FILE.cgi as processing instructions.
