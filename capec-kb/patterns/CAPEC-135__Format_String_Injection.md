# CAPEC-135: Format String Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/135.html  

## Description
An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must accept a strings as user input, fail to sanitize string formatting characters in the user input, and process this string using functions that interpret string formatting characters.

## Skills Required
- [High] In order to discover format string vulnerabilities it takes only low skill, however, converting this discovery into a working exploit requires advanced knowledge on the part of the adversary.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control; Impact: Gain Privileges
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Mitigations
- Limit the usage of formatting string functions.
- Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.

## Related Weaknesses (CWE)
- CWE-134
- CWE-20
- CWE-74
