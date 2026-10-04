# CAPEC-174: Flash Parameter Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/174.html  

## Description
An adversary takes advantage of improper data validation to inject malicious global parameters into a Flash file embedded within an HTML document. Flash files can leverage user-submitted data to configure the Flash document and access the embedding HTML document.

## Related Attack Patterns
- ChildOf: CAPEC-182
- CanAlsoBe: CAPEC-460
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-178

## Skills Required
- [Medium] The adversary need inject values into the global parameters to the Flash file and understand the parent HTML document DOM structure. The adversary needs to be smart enough to convince the victim to click on their crafted link.

## Resources Required
- The adversary must convince the victim to click their crafted link.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- User input must be sanitized according to context before reflected back to the user. The JavaScript function 'encodeURI' is not always sufficient for sanitizing input intended for global Flash parameters. Extreme caution should be taken when saving user input in Flash cookies. In such cases the Flash file itself will need to be fixed and recompiled, changing the name of the local shared objects (Flash cookies).

## Related Weaknesses (CWE)
- CWE-88
