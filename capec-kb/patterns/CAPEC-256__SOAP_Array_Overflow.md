# CAPEC-256: SOAP Array Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/256.html  

## Description
An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The targeted SOAP server must trust that the array size as stated in messages it receives is correct, but read through the entire content of the message regardless of the stated size of the array.

## Resources Required
- The attacker must be able to craft malformed SOAP messages, specifically, messages with arrays where the stated array size understates the actual size of the array in the message.

## Mitigations
- If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.

## Related Weaknesses (CWE)
- CWE-805
