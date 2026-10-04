# CWE-768: Incorrect Short Circuit Evaluation

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/768.html  

## Description
The product contains a conditional statement with multiple logical expressions in which one of the non-leading expressions may produce side effects. This may lead to an unexpected state in the program after the execution of the conditional, because short-circuiting logic may prevent the side effects from occurring.

## Extended Description
Usage of short circuit evaluation, though well-defined in the C standard, may alter control flow in a way that introduces logic errors that are difficult to detect, possibly causing errors later during the product's execution. If an attacker can discover such an inconsistency, it may be exploitable to gain arbitrary control over a system. If the first condition of an "or" statement is assumed to be true under normal circumstances, or if the first condition of an "and" statement is assumed to be false, then any subsequent conditional may contain its own logic errors that are not detected during code review or testing. Finally, the usage of short circuit evaluation may decrease the maintainability of the code.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Varies by Context — Widely varied consequences are possible if an attacker is aware of an unexpected state in the product after a conditional. It may lead to information exposure, a system crash, or even complete attacker control of the system.

## Potential Mitigations
- [Implementation] Minimizing the number of statements in a conditional that produce side effects will help to prevent the likelihood of short circuit evaluation to alter control flow in an unexpected way.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following function attempts to take a size value from a user and allocate an array of that size (we ignore bounds checking for simplicity). The function tries to initialize each spot with the value of its index, that is, A[len-1] = len - 1; A[len-2] = len - 2; ... A[1] = 1; A[0] = 0; However, since the programmer uses the prefix decrement operator, when the conditional is evaluated with i == 1, the decrement will result in a 0 value for the first part of the predicate, causing the second portion to be bypassed via short-circuit evaluation. This means we cannot be sure of what value will be in A[0] when we return the array to the user.
