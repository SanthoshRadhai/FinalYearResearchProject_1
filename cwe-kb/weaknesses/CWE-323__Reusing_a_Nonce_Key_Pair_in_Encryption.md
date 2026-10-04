# CWE-323: Reusing a Nonce, Key Pair in Encryption

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/323.html  

## Description
Nonces should be used for the present occasion and only once.

## Related Weaknesses
- ChildOf: CWE-344

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — Potentially a replay attack, in which an attacker could send the same data twice, could be crafted if nonces are allowed to be reused. This could allow a user to send a message which masquerades as a valid message from a valid user.

## Potential Mitigations
- [Implementation] Refuse to reuse nonce values.
- [Implementation] Use techniques such as requiring incrementing, time based and/or challenge response to assure uniqueness of nonces.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code takes a password, concatenates it with a nonce, then encrypts it before sending over a network:
- This code sends a command to a remote server, using an encrypted password and nonce to prove the command is from a trusted party:
