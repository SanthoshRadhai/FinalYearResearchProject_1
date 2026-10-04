# CWE-1173: Improper Use of Validation Framework

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1173.html  

## Description
The product does not use, or incorrectly uses, an input validation framework that is provided by the source language or an independent library.

## Extended Description
Many modern coding languages provide developers with input validation frameworks to make the task of input validation easier and less error-prone. These frameworks will automatically check all input against specified criteria and direct execution to error handlers when invalid input is received. The improper use (i.e., an incorrect implementation or missing altogether) of these frameworks is not directly exploitable, but can lead to an exploitable condition if proper input validation is not performed later in the product. Not using provided input validation frameworks can also hurt the maintainability of code as future developers may not recognize the downstream input validation being used in the place of the validation framework.

## Related Weaknesses
- ChildOf: CWE-20

## Common Consequences
- Scope: Integrity; Impact: Unexpected State — Unchecked input leads to cross-site scripting, process control, and SQL injection vulnerabilities, among others.

## Potential Mitigations
- [Implementation] Properly use provided input validation frameworks.

## Detection Methods
- [Automated Static Analysis] Some instances of improper input validation can be detected using automated static analysis. A static analysis tool might allow the user to specify which application-specific methods or functions perform input validation; the tool might also have built-in knowledge of validation frameworks such as Struts. The tool may then suppress or de-prioritize any associated warnings. This allows the analyst to focus on areas of the software in which input validation does not appear to be present. Except in the cases described in the previous paragraph, automated static analysis might not be able to recognize when proper input validation is being performed, leading to false positives - i.e., warnings that do not have any security consequences or require any code changes.
