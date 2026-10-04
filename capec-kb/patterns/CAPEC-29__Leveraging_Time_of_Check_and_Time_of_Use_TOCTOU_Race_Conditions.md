# CAPEC-29: Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/29.html  

## Description
This attack targets a race condition occurring between the time of check (state) for a resource and the time of use of a resource. A typical example is file access. The adversary can leverage a file access race condition by "running the race", meaning that they would modify the resource between the first time the target program accesses the file and the time the target program uses the file. During that period of time, the adversary could replace or modify the file, causing the application to behave unexpectedly.

## Related Attack Patterns
- ChildOf: CAPEC-26

## Prerequisites
- A resource is access/modified concurrently by multiple processes.
- The adversary is able to modify resource.
- A race condition exists while accessing a resource.

## Skills Required
- [Medium] This attack can get sophisticated since the attack has to occur within a short interval of time.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related Weaknesses (CWE)
- CWE-367
- CWE-368
- CWE-366
- CWE-370
- CWE-362
- CWE-662
- CWE-691
- CWE-663
- CWE-665
