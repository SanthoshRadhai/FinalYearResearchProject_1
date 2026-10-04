# CWE-627: Dynamic Variable Evaluation

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/627.html  

## Description
In a language where the user can influence the name of a variable at runtime, if the variable names are not controlled, an attacker can read or write to arbitrary variables, or access arbitrary functions.

## Extended Description
The resultant vulnerabilities depend on the behavior of the application, both at the crossover point and in any control/data flow that is reachable by the related variables or functions.

## Related Weaknesses
- ChildOf: CWE-914
- PeerOf: CWE-183

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Modify Application Data, Execute Unauthorized Code or Commands — An attacker could gain unauthorized access to internal program variables and execute arbitrary code.

## Potential Mitigations
- [Implementation] Refactor the code to avoid dynamic variable evaluation whenever possible.
- [Implementation] Use only allowlists of acceptable variable or function names.
- [Implementation] For function names, ensure that you are only calling functions that accept the proper number of arguments, to avoid unexpected null arguments.
