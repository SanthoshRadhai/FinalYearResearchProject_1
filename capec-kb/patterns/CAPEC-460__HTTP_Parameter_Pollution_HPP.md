# CAPEC-460: HTTP Parameter Pollution (HPP)

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/460.html  

## Description
An adversary adds duplicate HTTP GET/POST parameters by injecting query string delimiters. Via HPP it may be possible to override existing hardcoded HTTP parameters, modify the application behaviors, access and, potentially exploit, uncontrollable variables, and bypass input validation checkpoints and WAF rules.

## Related Attack Patterns
- ChildOf: CAPEC-15
- CanPrecede: CAPEC-676

## Prerequisites
- HTTP protocol is used with some GET/POST parameters passed

## Resources Required
- Any tool that enables intercepting and tampering with HTTP requests

## Mitigations
- Configuration: If using a Web Application Firewall (WAF), filters should be carefully configured to detect abnormal HTTP requests
- Design: Perform URL encoding
- Implementation: Use strict regular expressions in URL rewriting
- Implementation: Beware of multiple occurrences of a parameter in a Query String

## Related Weaknesses (CWE)
- CWE-88
- CWE-147
- CWE-235
