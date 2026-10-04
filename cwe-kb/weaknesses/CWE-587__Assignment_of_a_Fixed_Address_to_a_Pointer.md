# CWE-587: Assignment of a Fixed Address to a Pointer

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/587.html  

## Description
The product sets a pointer to a specific address other than NULL or 0.

## Extended Description
Using a fixed address is not portable, because that address will probably not be valid in all environments or platforms.

## Related Weaknesses
- ChildOf: CWE-344
- ChildOf: CWE-758

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — If one executes code at a known location, an attacker might be able to inject code there beforehand.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart, Reduce Maintainability, Reduce Reliability — If the code is ported to another platform or environment, the pointer is likely to be invalid and cause a crash.
- Scope: Confidentiality, Integrity; Impact: Read Memory, Modify Memory — The data at a known pointer location can be easily read or influenced by an attacker.

## Potential Mitigations
- [Implementation] Never set a pointer to a fixed address.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- This code assumes a particular function will always be found at a particular address. It assigns a pointer to that address and calls the function.
