# CWE-696: Incorrect Behavior Order

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/696.html  

## Description
The product performs multiple related behaviors, but the behaviors are performed in the wrong order in ways that may produce resultant weaknesses.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Demonstrative Examples (summary)
- The following code attempts to validate a given input path by checking it against an allowlist and then return the canonical path. In this specific case, the path is considered valid if it starts with the string "/safe_dir/".
- This function prints the contents of a specified file requested by a user.
- Assume that the module foo_bar implements a protected register. The register content is the asset. Only transactions made by user id (indicated by signal usr_id) 0x4 are allowed to modify the register contents. The signal grant_access is used to provide access.
