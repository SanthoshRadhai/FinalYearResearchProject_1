# CWE-514: Covert Channel

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/514.html  

## Description
A covert channel is a path that can be used to transfer information in a way not intended by the system's designers.

## Extended Description
Typically the system has not given authorization for the transmission and has no knowledge of its occurrence.

## Related Weaknesses
- ChildOf: CWE-1229

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Read Application Data, Bypass Protection Mechanism

## Detection Methods
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- In this example, the attacker observes how long an authentication takes when the user types in the correct password.
