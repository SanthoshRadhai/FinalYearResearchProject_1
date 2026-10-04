# CAPEC-278: Web Services Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/278.html  

## Description
An adversary manipulates a web service related protocol to cause a web application or service to react differently than intended. This can either be performed through the manipulation of call parameters to include unexpected values, or by changing the called function to one that should normally be restricted or limited. By leveraging this pattern of attack, the adversary is able to gain access to data or resources normally restricted, or to cause the application or service to crash.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Prerequisites
- The targeted application or service must rely on web service protocols in such a way that malicious manipulation of them can alter functionality.

## Resources Required
- The attacker must be able to manipulate the communications to the targeted application or service.

## Mitigations
- Design: Range, size and value and consistency verification for any arguments supplied to applications and services from external sources and devise appropriate error response.
- Design: Ensure that function calls that should not be called by an unprivileged user are not accessible to them.

## Related Weaknesses (CWE)
- CWE-707
