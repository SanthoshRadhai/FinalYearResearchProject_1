# CWE-331: Insufficient Entropy

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/331.html  

## Description
The product uses an algorithm or scheme that produces insufficient entropy, leaving patterns or clusters of values that are more likely to occur than others.

## Related Weaknesses
- ChildOf: CWE-330
- ChildOf: CWE-330

## Common Consequences
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — An attacker could guess the random numbers generated and could gain unauthorized access to a system if the random numbers are used for authentication and authorization.

## Potential Mitigations
- [Implementation] Determine the necessary entropy to adequately provide for randomness and predictability. This can be achieved by increasing the number of bits of objects such as keys and seeds.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code generates a unique random identifier for a user's session.
- The following code uses a statistical PRNG to create a URL for a receipt that remains active for some period of time after a purchase.
