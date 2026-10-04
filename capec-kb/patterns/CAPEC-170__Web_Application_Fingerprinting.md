# CAPEC-170: Web Application Fingerprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/170.html  

## Description
An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.

## Related Attack Patterns
- ChildOf: CAPEC-541

## Prerequisites
- Any web application can be fingerprinted. However, some configuration choices can limit the useful information an attacker may collect during a fingerprinting attack.

## Skills Required
- [Low] Attacker knows how to send HTTP request, SQL query to a web application.

## Resources Required
- While simple fingerprinting can be accomplished with only a web browser, for more thorough fingerprinting an attacker requires a variety of tools to collect information about the target. These tools might include protocol analyzers, web-site crawlers, and fuzzing tools. Footprinting a service adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide URL file extension.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Appropriately deal with error messages.
- Implementation: Obfuscate database type in Database API's error message.

## Related Weaknesses (CWE)
- CWE-497
