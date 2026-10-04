# CWE-333: Improper Handling of Insufficient Entropy in TRNG

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/333.html  

## Description
True random number generators (TRNG) generally have a limited source of entropy and therefore can fail or block.

## Extended Description
The rate at which true random numbers can be generated is limited. It is important that one uses them only when they are needed for security.

## Related Weaknesses
- ChildOf: CWE-331
- ChildOf: CWE-755

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — A program may crash or block if it runs out of random numbers.

## Potential Mitigations
- [Implementation] Rather than failing on a lack of random numbers, it is often preferable to wait for more numbers to be created.

## Demonstrative Examples (summary)
- This code uses a TRNG to generate a unique session id for new connections to a server:
