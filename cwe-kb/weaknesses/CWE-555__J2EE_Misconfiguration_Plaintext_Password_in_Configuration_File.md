# CWE-555: J2EE Misconfiguration: Plaintext Password in Configuration File

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/555.html  

## Description
The J2EE application stores a plaintext password in a configuration file.

## Extended Description
Storing a plaintext password in a configuration file allows anyone who can read the file to access the password-protected resource, making it an easy target for attackers.

## Related Weaknesses
- ChildOf: CWE-260

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Do not hardwire passwords into your software.
- [Architecture and Design] Use industry standard libraries to encrypt passwords before storage in configuration files.

## Demonstrative Examples (summary)
- Below is a snippet from a Java properties file in which the LDAP server password is stored in plaintext.
