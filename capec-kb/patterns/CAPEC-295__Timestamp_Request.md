# CAPEC-295: Timestamp Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/295.html  

## Description
This pattern of attack leverages standard requests to learn the exact time associated with a target system. An adversary may be able to use the timestamp returned from the target to attack time-based security algorithms, such as random number generators, or time-based authentication mechanisms.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send a timestamp request to a remote target and receive a response.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200
