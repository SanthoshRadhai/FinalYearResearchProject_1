# CWE-348: Use of Less Trusted Source

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/348.html  

## Description
The product has two different sources of the same data or information, but it uses the source that has less support for verification, is less trusted, or is less resistant to attack.

## Related Weaknesses
- ChildOf: CWE-345

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — An attacker could utilize the untrusted data source to bypass protection mechanisms and gain access to sensitive data.

## Demonstrative Examples (summary)
- This code attempts to limit the access of a page to certain IP Addresses. It checks the 'HTTP_X_FORWARDED_FOR' header in case an authorized user is sending the request through a proxy.
