# CAPEC-538: Open-Source Library Manipulation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/538.html  

## Description
Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software development projects. The adversary can have a particular system in mind to target, or the implantation can be the first stage of follow-on attacks on many systems.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the open source code base being used by the manufacturer in a system being developed or currently deployed at a victim location.

## Skills Required
- [High] Advanced knowledge about the inclusion and specific usage of an open source code project within system being targeted for infiltration.

## Related Weaknesses (CWE)
- CWE-494
- CWE-829
