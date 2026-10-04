# CAPEC-582: Route Disabling

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/582.html  

## Description
An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an "Internet kill switch" by those in control of critical infrastructure. This attack pattern differs from most other obstruction patterns by targeting the route itself, as opposed to the data passed over the route.

## Related Attack Patterns
- ChildOf: CAPEC-607

## Prerequisites
- The adversary requires knowledge of and access to network route.

## Consequences
- Scope: Availability; Impact: Other
