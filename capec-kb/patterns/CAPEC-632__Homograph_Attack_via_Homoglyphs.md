# CAPEC-632: Homograph Attack via Homoglyphs

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/632.html  

## Description
An adversary registers a domain name containing a homoglyph, leading the registered domain to appear the same as a trusted domain. A homograph attack leverages the fact that different characters among various character sets look the same to the user. Homograph attacks must generally be combined with other attacks, such as phishing attacks, in order to direct Internet traffic to the adversary-controlled destinations.

## Related Attack Patterns
- ChildOf: CAPEC-616
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills Required
- [Low] Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Utilize browsers that can warn users if URLs contain characters from different character sets.

## Related Weaknesses (CWE)
- CWE-1007
