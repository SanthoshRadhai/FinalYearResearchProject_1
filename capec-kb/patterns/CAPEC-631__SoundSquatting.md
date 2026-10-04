# CAPEC-631: SoundSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/631.html  

## Description
An adversary registers a domain name that sounds the same as a trusted domain, but has a different spelling. A SoundSquatting attack takes advantage of a user's confusion of the two words to direct Internet traffic to adversary-controlled destinations. SoundSquatting does not require an attack against the trusted domain or complicated reverse engineering.

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
- Purchase potential SoundSquatted domains and forward to legitimate domain.
