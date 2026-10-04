# CAPEC-124: Shared Resource Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/124.html  

## Description
An adversary exploits a resource shared between multiple applications, an application pool or hardware pin multiplexing to affect behavior. Resources may be shared between multiple applications or between multiple threads of a single application. Resource sharing is usually accomplished through mutual access to a single memory location or multiplexed hardware pins. If an adversary can manipulate this shared resource (usually by co-opting one of the applications or threads) the other applications or threads using the shared resource will often continue to trust the validity of the compromised shared resource and use it in their calculations. This can result in invalid trust assumptions, corruption of additional data through the normal operations of the other users of the shared resource, or even cause a crash or compromise of the sharing applications.

## Prerequisites
- The target applications, threads or functions must share resources between themselves.
- The adversary must be able to manipulate some piece of the shared resource either directly or indirectly and the other users of the data must accept the changed data as valid. Usually this requires that the adversary be able to compromise one of the sharing applications or threads in order to manipulate the shared data.

## Resources Required
- None: The attacker does not need any specialized resources to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-1189
- CWE-1331
