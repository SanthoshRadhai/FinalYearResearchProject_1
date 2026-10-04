# CWE-321: Use of Hard-coded Cryptographic Key

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/321.html  

## Description
The product uses a hard-coded, unchangeable cryptographic key.

## Related Weaknesses
- ChildOf: CWE-798
- ChildOf: CWE-798
- ChildOf: CWE-798

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Application Data — If hard-coded cryptographic keys are used, it is almost certain that malicious users will gain access through the account in question. The use of a hard-coded cryptographic key significantly increases the possibility that encrypted data may be recovered.

## Potential Mitigations
- [Architecture and Design] Prevention schemes mirror that of hard-coded password storage.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code examples attempt to verify a password using a hard-coded cryptographic key.
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
