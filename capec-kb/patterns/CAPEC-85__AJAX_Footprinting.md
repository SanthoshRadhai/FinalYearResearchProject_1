# CAPEC-85: AJAX Footprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/85.html  

## Description
This attack utilizes the frequent client-server roundtrips in Ajax conversation to scan a system. While Ajax does not open up new vulnerabilities per se, it does optimize them from an attacker point of view. A common first step for an attacker is to footprint the target environment to understand what attacks will work. Since footprinting relies on enumeration, the conversational pattern of rapid, multiple requests and responses that are typical in Ajax applications enable an attacker to look for many vulnerabilities, well-known ports, network locations and so on. The knowledge gained through Ajax fingerprinting can be used to support other attacks, such as XSS.

## Related Attack Patterns
- ChildOf: CAPEC-580
- CanPrecede: CAPEC-63

## Prerequisites
- The user must allow JavaScript to execute in their browser

## Skills Required
- [Medium] To land and launch a script on victim's machine with appropriate footprinting logic for enumerating services and vulnerabilities in JavaScript

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.

## Related Weaknesses (CWE)
- CWE-79
- CWE-113
- CWE-348
- CWE-96
- CWE-20
- CWE-116
- CWE-184
- CWE-86
- CWE-692
