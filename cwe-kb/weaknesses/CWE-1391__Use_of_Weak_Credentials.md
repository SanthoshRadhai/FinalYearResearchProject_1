# CWE-1391: Use of Weak Credentials

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1391.html  

## Description
The product uses weak credentials (such as a default key or hard-coded password) that can be calculated, derived, reused, or guessed by an attacker.

## Extended Description
By design, authentication protocols try to ensure that attackers must perform brute force attacks if they do not know the credentials such as a key or password. However, when these credentials are easily predictable or even fixed (as with default or hard-coded passwords and keys), then the attacker can defeat the mechanism without relying on brute force. Credentials may be weak for different reasons, such as: Hard-coded (i.e., static and unchangeable by the administrator) Default (i.e., the same static value across different deployments/installations, but able to be changed by the administrator) Predictable (i.e., generated in a way that produces unique credentials across deployments/installations, but can still be guessed with reasonable efficiency) Previously Compromised (i.e., "leaked" credentials that were published as part of a data breach) Even if a new, unique credential is intended to be generated for each product installation, if the generation is predictable, then that may also simplify guessing attacks.

## Related Weaknesses
- ChildOf: CWE-1390

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — An adversary could bypass intended authentication restrictions.

## Potential Mitigations
- [Architecture and Design, Operation] When the user changes or sets a password, check the password against a database of already compromised or breached passwords. These passwords are likely to be used in password guessing attacks.

## Demonstrative Examples (summary)
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
