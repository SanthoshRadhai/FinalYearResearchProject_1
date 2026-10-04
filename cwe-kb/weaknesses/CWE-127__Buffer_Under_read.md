# CWE-127: Buffer Under-read

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/127.html  

## Description
The product reads from a buffer using buffer access mechanisms such as indexes or pointers that reference memory locations prior to the targeted buffer.

## Related Weaknesses
- ChildOf: CWE-125
- ChildOf: CWE-786

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory
- Scope: Confidentiality; Impact: Bypass Protection Mechanism — By reading out-of-bounds memory, an attacker might be able to get secret values, such as memory addresses, which can bypass protection mechanisms such as ASLR in order to improve the reliability and likelihood of exploiting a separate weakness to achieve code execution instead of just denial of service.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- In the following code, the method retrieves a value from an array at a specific array index location that is given as an input parameter to the method
