# CWE-652: Improper Neutralization of Data within XQuery Expressions ('XQuery Injection')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/652.html  

## Description
The product uses external input to dynamically construct an XQuery expression used to retrieve data from an XML database, but it does not neutralize or incorrectly neutralizes that input. This allows an attacker to control the structure of the query.

## Extended Description
The net effect is that the attacker will have control over the information selected from the XML database and may use that ability to control application flow, modify logic, retrieve unauthorized data, or bypass important checks (e.g. authentication).

## Related Weaknesses
- ChildOf: CWE-943
- ChildOf: CWE-91

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — An attacker might be able to read sensitive information from the XML database.

## Potential Mitigations
- [Implementation] Use parameterized queries. This will help ensure separation between data plane and control plane.
- [Implementation] Properly validate user input. Reject data where appropriate, filter where appropriate and escape where appropriate. Make sure input that will be used in XQL queries is safe in that context.

## Demonstrative Examples (summary)
- An attacker may pass XQuery expressions embedded in an otherwise standard XML document. The attacker tunnels through the application entry point to target the resource access layer. The string below is an example of an attacker accessing the accounts.xml to request the service provider send all user names back. doc(accounts.xml)//user[name='*'] The attacks that are possible through XQuery are difficult to predict, if the data is not validated prior to executing the XQL.
