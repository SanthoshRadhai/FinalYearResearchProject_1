# CWE-684: Incorrect Provision of Specified Functionality

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/684.html  

## Description
The code does not function according to its published specifications, potentially leading to incorrect usage.

## Extended Description
When providing functionality to an external party, it is important that the product behaves in accordance with the details specified. When requirements of nuances are not documented, the functionality may produce unintended behaviors for the caller, possibly leading to an exploitable state.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Ensure that your code strictly conforms to specifications.

## Demonstrative Examples (summary)
- In the following snippet from a doPost() servlet method, the server returns "200 OK" (default) even if an error occurs.
- In the following example, an HTTP 404 status code is returned in the event of an IOException encountered in a Java servlet. A 404 code is typically meant to indicate a non-existent resource and would be somewhat misleading in this case.
