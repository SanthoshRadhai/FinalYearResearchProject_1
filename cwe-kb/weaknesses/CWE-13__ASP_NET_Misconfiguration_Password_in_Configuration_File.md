# CWE-13: ASP.NET Misconfiguration: Password in Configuration File

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/13.html  

## Description
Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers.

## Related Weaknesses
- ChildOf: CWE-260

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [Implementation] Credentials stored in configuration files should be encrypted, Use standard APIs and industry accepted algorithms to encrypt the credentials stored in configuration files.

## Demonstrative Examples (summary)
- The following example shows a portion of a configuration file for an ASP.Net application. This configuration file includes username and password information for a connection to a database, but the pair is stored in plaintext.
