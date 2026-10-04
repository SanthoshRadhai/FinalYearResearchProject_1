# CWE-522: Insufficiently Protected Credentials

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/522.html  

## Description
The product transmits or stores authentication credentials, but it uses an insecure method that is susceptible to unauthorized interception and/or retrieval.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-287
- ChildOf: CWE-668

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — An attacker could gain access to user accounts and access sensitive data used by the user accounts.

## Potential Mitigations
- [Architecture and Design] Use an appropriate security mechanism to protect the credentials.
- [Architecture and Design] Make appropriate use of cryptography to protect the credentials.
- [Implementation] Use industry standards to protect the credentials (e.g. LDAP, keystore, etc.).

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code changes a user's password.
- The following code reads a password from a properties file and uses the password to connect to a database.
- The following code reads a password from the registry and uses the password to create a new network credential.
- Both of these examples verify a password by comparing it to a stored compressed version.
- The following examples show a portion of properties and configuration files for Java and ASP.NET applications. The files include username and password information but they are stored in cleartext.
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
