# CWE-908: Use of Uninitialized Resource

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/908.html  

## Description
The product uses or accesses a resource that has not been initialized.

## Extended Description
When a resource has not been properly initialized, the product may behave unexpectedly. This may lead to a crash or invalid memory access, but the consequences vary depending on the type of resource and how it is used within the product.

## Related Weaknesses
- ChildOf: CWE-665
- ChildOf: CWE-665

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data — When reusing a resource such as memory or a program variable, the original contents of that resource may not be cleared before it is sent to an untrusted party.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — The uninitialized resource may contain values that cause program flow to change in ways that the programmer did not intend.

## Potential Mitigations
- [Implementation] Explicitly initialize the resource before use. If this is performed through an API function or standard procedure, follow all required steps.
- [Implementation] Pay close attention to complex conditionals that affect initialization, since some branches might not perform the initialization.
- [Implementation] Avoid race conditions (CWE-362) during initialization routines.
- [Build and Compilation] Run or compile the product with settings that generate warnings about uninitialized variables or data.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Here, a boolean initiailized field is consulted to ensure that initialization tasks are only completed once. However, the field is mistakenly set to true during static initialization, so the initialization code is never reached.
- The following code intends to limit certain operations to the administrator only.
- The following code intends to concatenate a string to a variable and print the string.
- This example will leave test_string in an unknown condition when i is the same value as err_val, because test_string is not initialized (CWE-456). Depending on where this code segment appears (e.g. within a function body), test_string might be random if it is stored on the heap or stack. If the variable is declared in static memory, it might be zero or NULL. Compiler optimization might contribute to the unpredictability of this address.
