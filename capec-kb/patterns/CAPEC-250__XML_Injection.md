# CAPEC-250: XML Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Reference:** https://capec.mitre.org/data/definitions/250.html  

## Description
An attacker utilizes crafted XML user-controllable input to probe, attack, and inject data into the XML database, using techniques similar to SQL injection. The user-controllable input can allow for unauthorized viewing of data, bypassing authentication or the front-end application for direct XML database access, and possibly altering database information.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- XML queries used to process user input and retrieve information stored in XML documents
- User-controllable input not properly sanitized

## Skills Required
- [Low] An attacker must have knowledge of XML syntax and constructs in order to successfully leverage XML Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related Weaknesses (CWE)
- CWE-91
- CWE-74
- CWE-20
- CWE-707
