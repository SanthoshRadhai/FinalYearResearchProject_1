# CWE-593: Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/593.html  

## Description
The product modifies the SSL context after connection creation has begun.

## Extended Description
If the program modifies the SSL_CTX object after creating SSL objects from it, there is the possibility that older SSL objects created from the original context could all be affected by that change.

## Related Weaknesses
- ChildOf: CWE-666
- ChildOf: CWE-1390

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — No authentication takes place in this process, bypassing an assumed protection of encryption.
- Scope: Confidentiality; Impact: Read Application Data — The encrypted communication between a user and a trusted host may be subject to a sniffing attack.

## Potential Mitigations
- [Architecture and Design] Use a language or a library that provides a cryptography framework at a higher level of abstraction.
- [Implementation] Most SSL_CTX functions have SSL counterparts that act on SSL-type objects.
- [Implementation] Applications should set up an SSL_CTX completely, before creating SSL objects from it.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
