# CWE-203: Observable Discrepancy

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/203.html  

## Description
The product behaves differently or sends different responses under different circumstances in a way that is observable to an unauthorized actor.

## Related Weaknesses
- ChildOf: CWE-200
- ChildOf: CWE-200

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Read Application Data, Bypass Protection Mechanism — An attacker can gain access to sensitive information about the system, including authentication information that may allow an attacker to gain access to the system. Other security-relevant information about the operation or internal state of the product may be revealed to an unauthorized actor, such as whether a particular operation was successful or not.
- Scope: Confidentiality; Impact: Read Application Data — In some cases, discrepancies can be used by attackers to form a side channel. When cryptographic primitives are vulnerable to side-channel attacks, this could be used to reveal unencrypted plaintext in the worst case.

## Potential Mitigations
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- [Implementation] Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not.

## Demonstrative Examples (summary)
- The following code checks validity of the supplied username and password and notifies the user of a successful or failed login.
- In this example, the attacker observes how long an authentication takes when the user types in the correct password.
- Non-uniform processing time causes timing channel.
- Suppose memory access patterns for an encryption routine are dependent on the secret key.
