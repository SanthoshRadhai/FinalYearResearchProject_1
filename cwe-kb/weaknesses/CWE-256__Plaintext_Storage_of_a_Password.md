# CWE-256: Plaintext Storage of a Password

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/256.html  

## Description
The product stores a password in plaintext within resources such as memory or files.

## Related Weaknesses
- ChildOf: CWE-522

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Storing a plaintext password in a configuration file allows anyone who can read the file to access the password-protected resource. In some contexts, even storage of a plaintext password in memory is considered a security risk if the password is not cleared immediately after it is used.

## Potential Mitigations
- [Architecture and Design] Avoid storing passwords in easily accessible locations.
- [Architecture and Design] Consider storing cryptographic hashes of passwords as an alternative to storing in plaintext.
- A programmer might attempt to remedy the password management problem by obscuring the password with an encoding function, such as base 64 encoding, but this effort does not adequately protect the password because the encoding can be detected and decoded easily.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code reads a password from a properties file and uses the password to connect to a database.
- The following code reads a password from the registry and uses the password to create a new network credential.
- The following examples show a portion of properties and configuration files for Java and ASP.NET applications. The files include username and password information but they are stored in cleartext.
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
