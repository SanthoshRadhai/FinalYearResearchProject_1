# CWE-686: Function Call With Incorrect Argument Type

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/686.html  

## Description
The product calls a function, procedure, or routine, but the caller specifies an argument that is the wrong data type, which may lead to resultant weaknesses.

## Extended Description
This weakness is most likely to occur in loosely typed languages, or in strongly typed languages in which the types of variable arguments cannot be enforced at compilation time, or where there is implicit casting.

## Related Weaknesses
- ChildOf: CWE-628

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Detection Methods
- [Other] Because this function call often produces incorrect behavior, it will usually be detected during testing or normal operation of the product.
