# CWE-598: Use of HTTP Request With Sensitive Query String

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/598.html  

## Description
The web application uses an HTTP method to process a request, but the request includes sensitive information in the query string.

## Related Weaknesses
- ChildOf: CWE-201

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — At a minimum, attackers can garner information from query strings that can be utilized in escalating their method of attack, such as information about the internal workings of the application or database column names. Successful exploitation of query string parameter vulnerabilities could lead to an attacker impersonating a legitimate user, obtaining proprietary data, or simply executing actions not intended by the application developers. Examples of sensitive information may include secrets such as session identifiers, passwords, access tokens, or API keys; Personally Identifiable Information (PII) such as email addresses or phone numbers; records or logs of private activities; communications that are expected to be private; etc. Successful exploitation of query string parameter vulnerabilities could lead to an attacker impersonating a legitimate user, obtaining proprietary data, or simply executing actions not intended by the application developers.

## Potential Mitigations
- [Implementation] When sending sensitive information, only include it in the request body or request headers instead of the query string. This may require avoiding use of GET requests.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
