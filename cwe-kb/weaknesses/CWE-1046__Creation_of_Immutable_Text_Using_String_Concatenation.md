# CWE-1046: Creation of Immutable Text Using String Concatenation

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1046.html  

## Description
The product creates an immutable text string using string concatenation operations.

## Extended Description
When building a string via a looping feature (e.g., a FOR or WHILE loop), the use of += to append to the existing string will result in the creation of a new object with each iteration, which can be inefficient in comparison with use of text buffer data elements.

## Related Weaknesses
- ChildOf: CWE-1176

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly. If the relevant code is reachable by an attacker, then this could be influenced to create performance problem.
