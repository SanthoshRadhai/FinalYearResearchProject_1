# CWE-914: Improper Control of Dynamically-Identified Variables

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/914.html  

## Description
The product does not properly restrict reading from or writing to dynamically-identified variables.

## Extended Description
Many languages offer powerful features that allow the programmer to access arbitrary variables that are specified by an input string. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can modify unintended variables that have security implications.

## Related Weaknesses
- ChildOf: CWE-99
- ChildOf: CWE-913

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data — An attacker could modify sensitive data or program variables.
- Scope: Integrity; Impact: Execute Unauthorized Code or Commands
- Scope: Other, Integrity; Impact: Varies by Context, Alter Execution Logic

## Potential Mitigations
- [Implementation] For any externally-influenced input, check the input against an allowlist of internal program variables that are allowed to be modified.
- [Implementation, Architecture and Design] Refactor the code so that internal program variables do not need to be dynamically identified.

## Demonstrative Examples (summary)
- This code uses the credentials sent in a POST request to login a user.
