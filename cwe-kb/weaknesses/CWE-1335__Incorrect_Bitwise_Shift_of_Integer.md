# CWE-1335: Incorrect Bitwise Shift of Integer

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1335.html  

## Description
An integer value is specified to be shifted by a negative amount or an amount greater than or equal to the number of bits contained in the value causing an unexpected or indeterminate result.

## Extended Description
Specifying a value to be shifted by a negative amount is undefined in various languages. Various computer architectures implement this action in different ways. The compilers and interpreters when generating code to accomplish a shift generally do not do a check for this issue. Specifying an over-shift, a shift greater than or equal to the number of bits contained in a value to be shifted, produces a result which varies by architecture and compiler. In some languages, this action is specifically listed as producing an undefined result.

## Related Weaknesses
- ChildOf: CWE-682

## Common Consequences
- Scope: Integrity; Impact: DoS: Crash, Exit, or Restart

## Potential Mitigations
- [Implementation] Implicitly or explicitly add checks and mitigation for negative or over-shift values.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- A negative shift amount for an x86 or x86_64 shift instruction will produce the number of bits to be shifted by taking a 2's-complement of the shift amount and effectively masking that amount to the lowest 6 bits for a 64 bit shift instruction.
