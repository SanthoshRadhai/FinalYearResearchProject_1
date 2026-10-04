# CAPEC-116: Excavation

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/116.html  

## Description
An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes.

## Related Attack Patterns
- CanPrecede: CAPEC-163

## Prerequisites
- An adversary requires some way of interacting with the system.

## Resources Required
- A tool, such as an Adversary in the Middle (CAPEC-94) Proxy or a fuzzer, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Minimize error/response output to only what is necessary for functional use or corrective language.
- Remove potentially sensitive information that is not necessary for the application's functionality.

## Related Weaknesses (CWE)
- CWE-200
- CWE-1243
