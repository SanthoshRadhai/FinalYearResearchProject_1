# CAPEC-204: Lifting Sensitive Data Embedded in Cache

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/204.html  

## Description
An adversary examines a target application's cache, or a browser cache, for sensitive information. Many applications that communicate with remote entities or which perform intensive calculations utilize caches to improve efficiency. However, if the application computes or receives sensitive information and the cache is not appropriately protected, an attacker can browse the cache and retrieve this information. This can result in the disclosure of sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-167
- CanPrecede: CAPEC-560

## Prerequisites
- The target application must store sensitive information in a cache.
- The cache must be inadequately protected against attacker access.

## Resources Required
- The attacker must be able to reach the target application's cache. This may require prior access to the machine on which the target application runs. If the cache is encrypted, the attacker would need sufficient computational resources to crack the encryption. With strong encryption schemes, doing this could be intractable, but weaker encryption schemes could allow an attacker with sufficient resources to read the file.

## Related Weaknesses (CWE)
- CWE-524
- CWE-311
- CWE-1239
- CWE-1258
