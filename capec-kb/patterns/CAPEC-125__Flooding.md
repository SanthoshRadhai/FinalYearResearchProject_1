# CAPEC-125: Flooding

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/125.html  

## Description
An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.

## Prerequisites
- Any target that services requests is vulnerable to this attack on some level of scale.

## Resources Required
- A script or program capable of generating more requests than the target can handle, or a network or cluster of objects all capable of making simultaneous requests.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Ensure that protocols have specific limits of scale configured.
- Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits.
- Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.

## Related Weaknesses (CWE)
- CWE-404
- CWE-770
