# CWE-188: Reliance on Data/Memory Layout

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/188.html  

## Description
The product makes invalid assumptions about how protocol data or memory is organized at a lower level, resulting in unintended program behavior.

## Extended Description
When changing platforms or protocol versions, in-memory organization of data may change in unintended ways. For example, some architectures may place local variables A and B right next to each other with A on top; some may place them next to each other with B on top; and others may add some padding to each. The padding size may vary to ensure that each variable is aligned to a proper word size. In protocol implementations, it is common to calculate an offset relative to another field to pick out a specific piece of data. Exceptional conditions, often involving new protocol versions, may add corner cases that change the data layout in an unusual way. The result can be that an implementation accesses an unintended field in the packet, treating data of one type as data of another type.

## Related Weaknesses
- ChildOf: CWE-1105
- ChildOf: CWE-435

## Common Consequences
- Scope: Integrity, Confidentiality; Impact: Modify Memory, Read Memory — Can result in unintended modifications or exposure of sensitive memory.

## Potential Mitigations
- [Implementation, Architecture and Design] In flat address space situations, never allow computing memory addresses as offsets from another memory address.
- [Architecture and Design] Fully specify protocol layout unambiguously, providing a structured grammar (e.g., a compilable yacc grammar).
- [Testing] Testing: Test that the implementation properly handles each case in the protocol grammar.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- In this example function, the memory address of variable b is derived by adding 1 to the address of variable a. This derived address is then used to assign the value 0 to b.
