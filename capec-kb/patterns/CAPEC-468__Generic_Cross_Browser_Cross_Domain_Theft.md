# CAPEC-468: Generic Cross-Browser Cross-Domain Theft

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/468.html  

## Description
An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ignore all data that does not make sense before a valid CSS descriptor is found by the CSS parser.

## Related Attack Patterns
- ChildOf: CAPEC-242

## Prerequisites
- No new lines can be present in the injected CSS stringProper HTML or URL escaping of the " and ' characters is not presentThe attacker has control of two injection points: pre-string and post-string

## Skills Required
- [High] Ability to craft a CSS injection

## Resources Required
- Attacker controlled site/page to render a page referencing the injected CSS string

## Mitigations
- Design: Prior to performing CSS parsing, require the CSS to start with well-formed CSS when it is a cross-domain load and the MIME type is broken. This is a browser level fix.
- Implementation: Perform proper HTML encoding and URL escaping

## Related Weaknesses (CWE)
- CWE-707
- CWE-149
- CWE-177
- CWE-838
