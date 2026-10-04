# CWE-234: Failure to Handle Missing Parameter

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/234.html  

## Description
If too few arguments are sent to a function, the function will still pop the expected number of arguments from the stack. Potentially, a variable number of arguments could be exhausted in a function as well.

## Related Weaknesses
- ChildOf: CWE-233

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity — There is the potential for arbitrary code execution with privileges of the vulnerable program if function parameter list is exhausted.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — Potentially a program could fail if it needs more arguments then are available.

## Potential Mitigations
- [Build and Compilation] This issue can be simply combated with the use of proper build process.
- [Implementation] Forward declare all functions. This is the recommended solution. Properly forward declaration of all used functions will result in a compiler error if too few arguments are sent to a function.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
