# CAPEC-584: BGP Route Disabling

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/584.html  

## Description
An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by selecting the most efficient route between Autonomous Systems (AS), or routing domains. BGP is the basis for interdomain routing infrastructure, providing connections between these ASs. By suppressing the intended AS routing advertisements and/or forcing less effective routes for traffic to ASs, the adversary can deny availability for the target network.

## Related Attack Patterns
- ChildOf: CAPEC-582

## Prerequisites
- The adversary must have control of a router that can modify, drop, or introduce spoofed BGP updates.The adversary can convince

## Resources Required
- BGP Router

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Implement Ingress filters to check the validity of received routes. However, this relies on the accuracy of Internet Routing Registries (IRRs) databases which are often not well-maintained.
- Implement Secure BGP (S-BGP protocol), which improves authorization and authentication capabilities based on public-key cryptography.
