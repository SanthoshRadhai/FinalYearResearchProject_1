# CAPEC-83: XPath Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/83.html  

## Description
An attacker can craft special user-controllable input consisting of XPath expressions to inject the XML database and bypass authentication or glean information that they normally would not be able to. XPath Injection enables an attacker to talk directly to the XML database, thus bypassing the application completely. XPath Injection results from the failure of an application to properly sanitize input used as part of dynamic XPath expressions used to query an XML database.

## Related Attack Patterns
- ChildOf: CAPEC-250

## Prerequisites
- XPath queries used to retrieve information stored in XML documents
- User-controllable input not properly sanitized before being used as part of XPath queries

## Skills Required
- [Low] XPath Injection shares the same basic premises with SQL Injection. An attacker must have knowledge of XPath syntax and constructs in order to successfully leverage XPath Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XPath expression. Characters such as a single-quote(') or operators such as or (|), and (&) and such should be filtered if the application does not expect them in the context in which they appear. If such content cannot be filtered, it must at least be properly escaped to avoid them being interpreted as part of XPath expressions.
- Use of parameterized XPath queries - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related Weaknesses (CWE)
- CWE-91
- CWE-74
- CWE-20
- CWE-707
