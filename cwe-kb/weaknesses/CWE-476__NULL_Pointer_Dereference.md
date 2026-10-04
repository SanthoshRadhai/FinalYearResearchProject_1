# CWE-476: NULL Pointer Dereference

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/476.html  

## Description
The product dereferences a pointer that it expects to be valid but is NULL.

## Related Weaknesses
- ChildOf: CWE-710
- ChildOf: CWE-754
- ChildOf: CWE-754

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — NULL pointer dereferences usually result in the failure of the process unless exception handling (on some platforms) is available and implemented. Even when exception handling is being used, it can still be very difficult to return the software to a safe state of operation.
- Scope: Integrity, Confidentiality; Impact: Execute Unauthorized Code or Commands, Read Memory, Modify Memory — In rare circumstances, when NULL is equivalent to the 0x0 memory address and privileged code can access it, then writing or reading memory is possible, which may lead to code execution.

## Potential Mitigations
- [Implementation] For any pointers that could have been modified or provided from a function that can return NULL, check the pointer for NULL before use. When working with a multithreaded or otherwise asynchronous environment, ensure that proper locking APIs are used to lock before the check, and unlock when it has finished [REF-1484].
- [Requirements] Select a programming language that is not susceptible to these issues.
- [Implementation] Check the results of all functions that return a value and verify that the value is non-null before acting upon it.
- [Architecture and Design] Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.
- [Implementation] Explicitly initialize all variables and other data stores, either during declaration or just before the first usage.

## Detection Methods
- [Automated Dynamic Analysis] This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- [Manual Dynamic Analysis] Identify error conditions that are not likely to occur during normal usage and trigger them. For example, run the program under low memory conditions, run with insufficient privileges or permissions, interrupt a transaction before it is completed, or disable connectivity to basic network services such as DNS. Monitor the software for any unexpected behavior. If you trigger an unhandled exception or similar error that was discovered and handled by the application's environment, it may still indicate unexpected conditions that were not handled by the application itself.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- This example takes an IP address from a user, verifies that it is well formed and then looks up the hostname and copies it into a buffer.
- In the following code, the programmer assumes that the system always has a property named "cmd" defined. If an attacker can control the program's environment so that "cmd" is not defined, the program throws a NULL pointer exception when it attempts to call the trim() method.
- This Android application has registered to handle a URL when sent an intent:
- Consider the following example of a typical client server exchange. The HandleRequest function is intended to perform a request and use a defer to close the connection whenever the function returns.
