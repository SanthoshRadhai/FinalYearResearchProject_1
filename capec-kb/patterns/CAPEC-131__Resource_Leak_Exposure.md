# CAPEC-131: Resource Leak Exposure

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/131.html  

## Description
An adversary utilizes a resource leak on the target to deplete the quantity of the resource available to service legitimate requests.

## Prerequisites
- The target must have a resource leak that the adversary can repeatedly trigger.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- If possible, leverage coding language(s) that do not allow this weakness to occur (e.g., Java, Ruby, and Python all perform automatic garbage collection that releases memory for objects that have been deallocated).
- Memory should always be allocated/freed using matching functions (e.g., malloc/free, new/delete, etc.)
- Implement best practices with respect to memory management, including the freeing of all allocated resources at all exit points and ensuring consistency with how and where memory is freed in a function.

## Related Weaknesses (CWE)
- CWE-404
