# CAPEC-198: XSS Targeting Error Pages

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/198.html  

## Description
An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- A third party web server which fails to adequately sanitize messages sent in error pages.
- The victim must be made to execute a query crafted by the adversary which results in the infected error report.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be used in error messages.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-81
