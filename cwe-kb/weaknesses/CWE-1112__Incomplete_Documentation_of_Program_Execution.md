# CWE-1112: Incomplete Documentation of Program Execution

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1112.html  

## Description
The document does not fully define all mechanisms that are used to control or influence how product-specific programs are executed.

## Extended Description
This includes environmental variables, configuration files, registry keys, command-line switches or options, or system settings.

## Related Weaknesses
- ChildOf: CWE-1059

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability
- Scope: Other; Impact: Increase Analytical Complexity
