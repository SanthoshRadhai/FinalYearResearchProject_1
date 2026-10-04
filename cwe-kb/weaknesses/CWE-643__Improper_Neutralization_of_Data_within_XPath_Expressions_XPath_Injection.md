# CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/643.html  

## Description
The product uses external input to dynamically construct an XPath expression used to retrieve data from an XML database, but it does not neutralize or incorrectly neutralizes that input. This allows an attacker to control the structure of the query.

## Extended Description
The net effect is that the attacker will have control over the information selected from the XML database and may use that ability to control application flow, modify logic, retrieve unauthorized data, or bypass important checks (e.g. authentication).

## Related Weaknesses
- ChildOf: CWE-943
- ChildOf: CWE-91

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — Controlling application flow (e.g. bypassing authentication).
- Scope: Confidentiality; Impact: Read Application Data — The attacker could read restricted XML content.

## Potential Mitigations
- [Implementation] Use parameterized XPath queries (e.g. using XQuery). This will help ensure separation between data plane and control plane.
- [Implementation] Properly validate user input. Reject data where appropriate, filter where appropriate and escape where appropriate. Make sure input that will be used in XPath queries is safe in that context.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Consider the following simple XML document that stores authentication information and a snippet of Java code that uses XPath query to retrieve authentication information:
