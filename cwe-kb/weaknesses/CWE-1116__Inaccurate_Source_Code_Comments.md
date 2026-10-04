# CWE-1116: Inaccurate Source Code Comments

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1116.html  

## Description
The source code contains comments that do not accurately describe or explain aspects of the portion of the code with which the comment is associated.

## Related Weaknesses
- ChildOf: CWE-1078

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
- Scope: Other; Impact: Increase Analytical Complexity — When a comment does not accurately reflect the associated code elements, this can introduce confusion to a reviewer (due to inconsistencies) or make it more difficult and less efficient to validate that the code is implementing the intended behavior correctly.

## Potential Mitigations
- [Implementation] Verify that each comment accurately reflects what is intended to happen during execution of the code.

## Demonstrative Examples (summary)
- In the following Java example the code performs a calculation to determine how much medicine to administer. A comment is provided to give insight into what the calculation shoud be doing. Unfortunately the comment does not match the actual code and thus leaves the reader to wonder which is correct.
