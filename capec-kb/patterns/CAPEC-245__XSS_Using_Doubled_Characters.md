# CAPEC-245: XSS Using Doubled Characters

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/245.html  

## Description
The adversary bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the adversary can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The targeted web application does not fully normalize input before checking for prohibited syntax. In particular, it must fail to recognize prohibited methods preceded by certain sequences of repeated characters.

## Resources Required
- The adversary must trick the victim into following a crafted link to a vulnerable server or view a web post where the dangerous commands are executed.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and sanitize all user supplied fields.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-85
