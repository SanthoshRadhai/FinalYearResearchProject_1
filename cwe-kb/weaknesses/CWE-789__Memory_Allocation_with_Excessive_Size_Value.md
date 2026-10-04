# CWE-789: Memory Allocation with Excessive Size Value

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/789.html  

## Description
The product allocates memory based on an untrusted, large size value, but it does not ensure that the size is within expected limits, allowing arbitrary amounts of memory to be allocated.

## Related Weaknesses
- ChildOf: CWE-770
- CanPrecede: CWE-476

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (Memory) — Not controlling memory allocation can result in a request for too much system memory, possibly leading to a crash of the application due to out-of-memory conditions, or the consumption of a large amount of memory on the system.

## Potential Mitigations
- [Implementation, Architecture and Design] Perform adequate input validation against any value that influences the amount of memory that is allocated. Define an appropriate strategy for handling requests that exceed the limit, and consider supporting a configuration option so that the administrator can extend the amount of memory to be used if necessary.
- [Operation] Run your program using system-provided resource limits for memory. This might still cause the program to crash or exit, but the impact to the rest of the system will be minimized.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- Consider the following code, which accepts an untrusted size value and allocates a buffer to contain a string of the given size.
- Consider the following code, which accepts an untrusted size value and uses the size as an initial capacity for a HashMap.
- This code performs a stack allocation based on a length calculation.
- This example shows a typical attempt to parse a string with an error resulting from a difference in assumptions between the caller to a function and the function's action.
- The following code obtains an untrusted number that is used as an index into an array of messages.
- This example shows a typical attempt to parse a string with an error resulting from a difference in assumptions between the caller to a function and the function's action. The buffer length ends up being -1 resulting in a blown out stack. The space character after the colon is included in the function calculation, but not in the caller's calculation. This, unfortunately, is not usually so obvious but exists in an obtuse series of calculations.
