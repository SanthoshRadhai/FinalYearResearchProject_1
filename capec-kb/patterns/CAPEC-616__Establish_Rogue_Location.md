# CAPEC-616: Establish Rogue Location

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/616.html  

## Description
An adversary provides a malicious version of a resource at a location that is similar to the expected location of a legitimate resource. After establishing the rogue location, the adversary waits for a victim to visit the location and access the malicious resource.

## Related Attack Patterns
- ChildOf: CAPEC-154
- CanPrecede: CAPEC-691

## Prerequisites
- A resource is expected to available to the user.

## Skills Required
- [Low] Adversaries can often purchase low-cost technology to implement rogue access points.

## Consequences
- Scope: Confidentiality, Integrity; Impact: Other

## Related Weaknesses (CWE)
- CWE-200
