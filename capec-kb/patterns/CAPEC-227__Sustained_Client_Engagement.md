# CAPEC-227: Sustained Client Engagement

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/227.html  

## Description
An adversary attempts to deny legitimate users access to a resource by continually engaging a specific resource in an attempt to keep the resource tied up as long as possible. The adversary's primary goal is not to crash or flood the target, which would alert defenders; rather it is to repeatedly perform actions or abuse algorithmic flaws such that a given resource is tied up and not available to a legitimate user. By carefully crafting a requests that keep the resource engaged through what is seemingly benign requests, legitimate users are limited or completely denied access to the resource.

## Prerequisites
- This pattern of attack requires a temporal aspect to the servicing of a given request. Success can be achieved if the adversary can make requests that collectively take more time to complete than legitimate user requests within the same time frame.

## Resources Required
- To successfully execute this pattern of attack, a script or program is often required that is capable of continually engaging the target and maintaining sustained usage of a specific resource. Depending on the configuration of the target, it may or may not be necessary to involve a network or cluster of objects all capable of making parallel requests.

## Mitigations
- Potential mitigations include requiring a unique login for each resource request, constraining local unprivileged access by disallowing simultaneous engagements of the resource, or limiting access to the resource to one access per IP address. In such scenarios, the adversary would have to increase engagements either by launching multiple sessions manually or programmatically to counter such defenses.

## Related Weaknesses (CWE)
- CWE-400
