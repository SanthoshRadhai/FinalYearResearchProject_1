# CWE-185: Incorrect Regular Expression

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/185.html  

## Description
The product specifies a regular expression in a way that causes data to be improperly matched or compared.

## Extended Description
When the regular expression is used in protection mechanisms such as filtering or validation, this may allow an attacker to bypass the intended restrictions on the incoming data.

## Related Weaknesses
- ChildOf: CWE-697
- CanPrecede: CWE-187
- CanPrecede: CWE-182

## Common Consequences
- Scope: Other; Impact: Unexpected State, Varies by Context — When the regular expression is not correctly specified, data might have a different format or type than the rest of the program expects, producing resultant weaknesses or errors.
- Scope: Access Control; Impact: Bypass Protection Mechanism — In PHP, regular expression checks can sometimes be bypassed with a null byte, leading to any number of weaknesses.

## Potential Mitigations
- [Implementation] Regular expressions can become error prone when defining a complex language even for those experienced in writing grammars. Determine if several smaller regular expressions simplify one large regular expression. Also, subject the regular expression to thorough testing techniques such as equivalence partitioning, boundary value analysis, and robustness. After testing and a reasonable confidence level is achieved, a regular expression may not be foolproof. If an exploit is allowed to slip through, then record the exploit and refactor the regular expression.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code takes phone numbers as input, and uses a regular expression to reject invalid phone numbers.
- This code uses a regular expression to validate an IP string prior to using it in a call to the "ping" command.
