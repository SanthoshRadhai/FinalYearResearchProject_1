# CAPEC-630: TypoSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/630.html  

## Description
An adversary registers a domain name with at least one character different than a trusted domain. A TypoSquatting attack takes advantage of instances where a user mistypes a URL (e.g. www.goggle.com) or not does visually verify a URL before clicking on it (e.g. phishing attack). As a result, the user is directed to an adversary-controlled destination. TypoSquatting does not require an attack against the trusted domain or complicated reverse engineering.

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
- Purchase potential TypoSquatted domains and forward to legitimate domain.
