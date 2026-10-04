# CAPEC-130: Excessive Allocation

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/130.html  

## Description
An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.

## Prerequisites
- The target must accept service requests from the attacker and the adversary must be able to control the resource allocation associated with this request to be in excess of the normal allocation. The latter is usually accomplished through the presence of a bug on the target that allows the adversary to manipulate variables used in the allocation.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Limit the amount of resources that are accessible to unprivileged users.
- Assume all input is malicious. Consider all potentially relevant properties when validating input.
- Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- Use resource-limiting settings, if possible.

## Related Weaknesses (CWE)
- CWE-404
- CWE-770
- CWE-1325
