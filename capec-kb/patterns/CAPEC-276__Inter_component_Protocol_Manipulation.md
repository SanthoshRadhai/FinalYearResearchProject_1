# CAPEC-276: Inter-component Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/276.html  

## Description
Inter-component protocols are used to communicate between different software and hardware modules within a single computer. Common examples are: interrupt signals and data pipes. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Related Weaknesses (CWE)
- CWE-707
