# CWE-196: Unsigned to Signed Conversion Error

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/196.html  

## Description
The product uses an unsigned primitive and performs a cast to a signed primitive, which can produce an unexpected value if the value of the unsigned primitive can not be represented using a signed primitive.

## Extended Description
Although less frequent an issue than signed-to-unsigned conversion, unsigned-to-signed conversion can be the perfect precursor to dangerous buffer underwrite conditions that allow attackers to move down the stack where they otherwise might not have access in a normal buffer overflow condition. Buffer underwrites occur frequently when large unsigned values are cast to signed values, and then used as indexes into a buffer or for pointer arithmetic.

## Related Weaknesses
- ChildOf: CWE-681
- ChildOf: CWE-681
- ChildOf: CWE-681
- CanAlsoBe: CWE-124
- CanAlsoBe: CWE-120

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — Incorrect sign conversions generally lead to undefined behavior, and therefore crashes.
- Scope: Integrity; Impact: Modify Memory — If a poor cast lead to a buffer overflow or similar condition, data integrity may be affected.
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism — Improper signed-to-unsigned conversions without proper checking can sometimes trigger buffer overflows which can be used to execute arbitrary code. This is usually outside the scope of a program's implicit security policy.

## Potential Mitigations
- [Requirements] Choose a language which is not subject to these casting flaws.
- [Architecture and Design] Design object accessor functions to implicitly check values for valid sizes. Ensure that all functions which will be used as a size are checked previous to use as a size. If the language permits, throw exceptions rather than using in-band errors.
- [Implementation] Error check the return values of all functions. Be aware of implicit casts made, and use unsigned variables for sizes if at all possible.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
