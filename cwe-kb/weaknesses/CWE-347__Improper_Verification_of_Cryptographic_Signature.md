# CWE-347: Improper Verification of Cryptographic Signature

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/347.html  

## Description
The product does not verify, or incorrectly verifies, the cryptographic signature for data.

## Related Weaknesses
- ChildOf: CWE-345
- ChildOf: CWE-345

## Common Consequences
- Scope: Access Control, Integrity, Confidentiality; Impact: Gain Privileges or Assume Identity, Modify Application Data, Execute Unauthorized Code or Commands — An attacker could gain access to sensitive data and possibly execute unauthorized code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code, a JarFile object is created from a downloaded file.
