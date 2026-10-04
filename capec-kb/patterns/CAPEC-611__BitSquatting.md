# CAPEC-611: BitSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/611.html  

## Description
An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is operating system and architecture agnostic. Experimental observations show that BitSquatting popular websites could redirect non-trivial amounts of Internet traffic to a malicious entity.

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
- When possible, use error-correcting (ECC) memory in local devices as non-ECC memory is significantly more vulnerable to faults.
