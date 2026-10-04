# CWE-409: Improper Handling of Highly Compressed Data (Data Amplification)

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/409.html  

## Description
The product does not handle or incorrectly handles a compressed input with a very high compression ratio that produces a large output.

## Extended Description
An example of data amplification is a "decompression bomb," a small ZIP file that can produce a large amount of data when it is decompressed.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Availability; Impact: DoS: Amplification, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — System resources, CPU and memory, can be quickly consumed. This can lead to poor system performance or system crash.

## Demonstrative Examples (summary)
- The DTD and the very brief XML below illustrate what is meant by an XML bomb. The ZERO entity contains one character, the letter A. The choice of entity name ZERO is being used to indicate length equivalent to that exponent on two, that is, the length of ZERO is 2^0. Similarly, ONE refers to ZERO twice, therefore the XML parser will expand ONE to a length of 2, or 2^1. Ultimately, we reach entity THIRTYTWO, which will expand to 2^32 characters in length, or 4 GB, probably consuming far more data than expected.
