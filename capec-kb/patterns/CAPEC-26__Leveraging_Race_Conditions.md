# CAPEC-26: Leveraging Race Conditions

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/26.html  

## Description
The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by "running the race", modifying the resource and modifying the normal execution flow. For instance, a race condition can occur while accessing a file: the adversary can trick the system by replacing the original file with their version and cause the system to read the malicious file.

## Prerequisites
- A resource is accessed/modified concurrently by multiple processes such that a race condition exists.
- The adversary has the ability to modify the resource.

## Skills Required
- [Medium] Being able to "run the race" requires basic knowledge of concurrent processing including synchonization techniques.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related Weaknesses (CWE)
- CWE-368
- CWE-363
- CWE-366
- CWE-370
- CWE-362
- CWE-662
- CWE-689
- CWE-667
- CWE-665
- CWE-1223
- CWE-1254
- CWE-1298
