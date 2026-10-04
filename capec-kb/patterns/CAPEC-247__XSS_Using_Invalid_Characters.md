# CAPEC-247: XSS Using Invalid Characters

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/247.html  

## Description
An adversary inserts invalid characters in identifiers to bypass application filtering of input. Filters may not scan beyond invalid characters but during later stages of processing content that follows these invalid characters may still be processed. This allows the adversary to sneak prohibited commands past filters and perform normally prohibited operations. Invalid characters may include null, carriage return, line feed or tab in an identifier. Successful bypassing of the filter can result in a XSS attack, resulting in the disclosure of web cookies or possibly other results.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The target must fail to remove invalid characters from input and fail to adequately scan beyond these characters.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be included in any subsequent web pages or back end operations.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-86
