# CAPEC-456: Infected Memory

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/456.html  

## Description
An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems that are still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect stop operations with known virus.

## Related Weaknesses (CWE)
- CWE-1257
- CWE-1260
- CWE-1274
- CWE-1312
- CWE-1316
