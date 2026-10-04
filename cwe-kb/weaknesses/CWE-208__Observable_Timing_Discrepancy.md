# CWE-208: Observable Timing Discrepancy

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/208.html  

## Description
Two separate operations in a product require different amounts of time to complete, in a way that is observable to an actor and reveals security-relevant information about the state of the product, such as whether a particular operation was successful or not.

## Extended Description
In security-relevant contexts, even small variations in timing can be exploited by attackers to indirectly infer certain details about the product's internal operations. For example, in some cryptographic algorithms, attackers can use timing differences to infer certain properties about a private key, making the key easier to guess. Timing discrepancies effectively form a timing side channel.

## Related Weaknesses
- ChildOf: CWE-203
- CanPrecede: CWE-385
- CanPrecede: CWE-327

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Read Application Data, Bypass Protection Mechanism

## Demonstrative Examples (summary)
- Consider an example hardware module that checks a user-provided password to grant access to a user. The user-provided password is compared against a golden value in a byte-by-byte manner.
- In this example, the attacker observes how long an authentication takes when the user types in the correct password.
