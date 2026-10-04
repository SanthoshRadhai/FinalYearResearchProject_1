# CWE-1235: Incorrect Use of Autoboxing and Unboxing for Performance Critical Operations

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1235.html  

## Description
The code uses boxed primitives, which may introduce inefficiencies into performance-critical operations.

## Related Weaknesses
- ChildOf: CWE-400

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Reduce Performance — Incorrect autoboxing/unboxing would result in reduced performance, which sometimes can lead to resource consumption issues, impacting availability when used with generic collections.

## Potential Mitigations
- [Implementation] Use of boxed primitives should be limited to certain situations such as when calling methods with typed parameters. They should not be used for scientific computing or other performance critical operations. They are only suited to support "impedance mismatch" between reference types and primitives. Examine the use of boxed primitives prior to use. Use SparseArrays or ArrayMap instead of HashMap to avoid performance overhead.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Java has a boxed primitive for each primitive type. A long can be represented with the boxed primitive Long. Issues arise where boxed primitives are used when not strictly necessary.
- This code uses primitive long which fixes the issue.
