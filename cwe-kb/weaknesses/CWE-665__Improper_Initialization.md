# CWE-665: Improper Initialization

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/665.html  

## Description
The product does not initialize or incorrectly initializes a resource, which might leave the resource in an unexpected state when it is accessed or used.

## Extended Description
This can have security implications when the associated resource is expected to have certain properties or values, such as a variable that determines whether a user has been authenticated or not.

## Related Weaknesses
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data — When reusing a resource such as memory or a program variable, the original contents of that resource may not be cleared before it is sent to an untrusted party.
- Scope: Access Control; Impact: Bypass Protection Mechanism — If security-critical decisions rely on a variable having a "0" or equivalent value, and the programming language performs this initialization on behalf of the programmer, then a bypass of security may occur.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — The uninitialized data may contain values that cause program flow to change in ways that the programmer did not intend. For example, if an uninitialized variable is used as an array index in C, then its previous contents may produce an index that is outside the range of the array, possibly causing a crash or an exit in other environments.

## Potential Mitigations
- [Requirements] Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, in Java, if the programmer does not explicitly initialize a variable, then the code could produce a compile-time error (if the variable is local) or automatically initialize the variable to the default value for the variable's type. In Perl, if explicit initialization is not performed, then a default value of undef is assigned, which is interpreted as 0, false, or an equivalent value depending on the context in which the variable is accessed.
- [Architecture and Design] Identify all variables and data stores that receive information from external sources, and apply input validation to make sure that they are only initialized to expected values.
- [Implementation] Explicitly initialize all your variables and other data stores, either during declaration or just before the first usage.
- [Implementation] Pay close attention to complex conditionals that affect initialization, since some conditions might not perform the initialization.
- [Implementation] Avoid race conditions (CWE-362) during initialization routines.
- [Build and Compilation] Run or compile your product with settings that generate warnings about uninitialized variables or data.

## Detection Methods
- [Automated Dynamic Analysis] This weakness can be detected using dynamic tools and techniques that interact with the software using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results. Initialization problems may be detected with a stress-test by calling the software simultaneously from a large number of threads or processes, and look for evidence of any unexpected behavior. The software's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- [Manual Dynamic Analysis] Identify error conditions that are not likely to occur during normal usage and trigger them. For example, run the program under low memory conditions, run with insufficient privileges or permissions, interrupt a transaction before it is completed, or disable connectivity to basic network services such as DNS. Monitor the software for any unexpected behavior. If you trigger an unhandled exception or similar error that was discovered and handled by the application's environment, it may still indicate unexpected conditions that were not handled by the application itself.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Here, a boolean initiailized field is consulted to ensure that initialization tasks are only completed once. However, the field is mistakenly set to true during static initialization, so the initialization code is never reached.
- The following code intends to limit certain operations to the administrator only.
- The following code intends to concatenate a string to a variable and print the string.
