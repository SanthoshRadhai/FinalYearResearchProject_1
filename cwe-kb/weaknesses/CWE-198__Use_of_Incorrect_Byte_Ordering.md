# CWE-198: Use of Incorrect Byte Ordering

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/198.html  

## Description
The product receives input from an upstream component, but it does not account for byte ordering (e.g. big-endian and little-endian) when processing the input, causing an incorrect number or value to be used.

## Related Weaknesses
- ChildOf: CWE-188

## Common Consequences
- Scope: Integrity; Impact: Unexpected State

## Detection Methods
- [Black Box] Because byte ordering bugs are usually very noticeable even with normal inputs, this bug is more likely to occur in rarely triggered error conditions, making them difficult to detect using black box methods.
