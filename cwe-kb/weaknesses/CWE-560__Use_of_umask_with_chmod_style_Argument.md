# CWE-560: Use of umask() with chmod-style Argument

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/560.html  

## Description
The product calls umask() with an incorrect argument that is specified as if it is an argument to chmod().

## Related Weaknesses
- ChildOf: CWE-687

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control; Impact: Read Files or Directories, Modify Files or Directories, Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] Use umask() with the correct argument.

## Detection Methods
- [Automated Static Analysis] If you suspect misuse of umask(), you can use grep to spot call instances of umask().
