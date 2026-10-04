# CWE-589: Call to Non-ubiquitous API

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/589.html  

## Description
The product uses an API function that does not exist on all versions of the target platform. This could cause portability problems or inconsistencies that allow denial of service or other consequences.

## Extended Description
Some functions that offer security features supported by the OS are not available on all versions of the OS in common use. Likewise, functions are often deprecated or made obsolete for security reasons and should not be used.

## Related Weaknesses
- ChildOf: CWE-474

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Always test your code on any platform on which it is targeted to run on.
- [Testing] Test your code on the newest and oldest platform on which it is targeted to run on.
- [Testing] Develop a system to test for API functions that are not portable.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
