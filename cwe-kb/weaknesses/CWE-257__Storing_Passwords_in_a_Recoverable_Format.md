# CWE-257: Storing Passwords in a Recoverable Format

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/257.html  

## Description
The storage of passwords in a recoverable format makes them subject to password reuse attacks by malicious users. In fact, it should be noted that recoverable encrypted passwords provide no significant benefit over plaintext passwords since they are subject not only to reuse by malicious attackers but also by malicious insiders. If a system administrator can recover a password directly, or use a brute force search on the available information, the administrator can use the password on other accounts.

## Related Weaknesses
- ChildOf: CWE-522
- PeerOf: CWE-259

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Gain Privileges or Assume Identity — User's passwords may be revealed.
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Revealed passwords may be reused elsewhere to impersonate the users in question.

## Potential Mitigations
- [Architecture and Design] Use strong, non-reversible encryption to protect stored passwords.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Both of these examples verify a password by comparing it to a stored compressed version.
- The following examples show a portion of properties and configuration files for Java and ASP.NET applications. The files include username and password information but they are stored in cleartext.
