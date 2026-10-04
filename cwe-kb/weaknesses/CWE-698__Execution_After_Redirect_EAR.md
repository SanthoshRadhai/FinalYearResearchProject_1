# CWE-698: Execution After Redirect (EAR)

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/698.html  

## Description
The web application sends a redirect to another location, but instead of exiting, it executes additional code.

## Related Weaknesses
- ChildOf: CWE-705
- ChildOf: CWE-670

## Common Consequences
- Scope: Other, Confidentiality, Integrity, Availability; Impact: Alter Execution Logic, Execute Unauthorized Code or Commands — This weakness could affect the control flow of the application and allow execution of untrusted code.

## Detection Methods
- [Black Box] This issue might not be detected if testing is performed using a web browser, because the browser might obey the redirect and move the user to a different page before the application has produced outputs that indicate something is amiss.

## Demonstrative Examples (summary)
- This code queries a server and displays its status when a request comes from an authorized IP address.
