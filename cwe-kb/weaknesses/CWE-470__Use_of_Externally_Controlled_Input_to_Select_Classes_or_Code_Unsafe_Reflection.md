# CWE-470: Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/470.html  

## Description
The product uses external input with reflection to select which classes or code to use, but it does not sufficiently prevent the input from selecting improper classes or code.

## Extended Description
If the product uses external inputs to determine which class to instantiate or which method to invoke, then an attacker could supply values to select unexpected classes or methods. If this occurs, then the attacker could create control flow paths that were not intended by the developer. These paths could bypass authentication or access control checks, or otherwise cause the product to behave in an unexpected manner. This situation becomes a doomsday scenario if the attacker can upload files into a location that appears on the product's classpath (CWE-427) or add new entries to the product's classpath (CWE-426). Under either of these conditions, the attacker can use reflection to introduce new, malicious behavior into the product.

## Related Weaknesses
- ChildOf: CWE-913
- ChildOf: CWE-913
- ChildOf: CWE-610
- ChildOf: CWE-20

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Other; Impact: Execute Unauthorized Code or Commands, Alter Execution Logic — The attacker might be able to execute code that is not directly accessible to the attacker. Alternately, the attacker could call unexpected code in the wrong place or the wrong time, possibly modifying critical system state.
- Scope: Availability, Other; Impact: DoS: Crash, Exit, or Restart, Other — The attacker might be able to use reflection to call the wrong code, possibly with unexpected arguments that violate the API (CWE-227). This could cause the product to exit or hang.
- Scope: Confidentiality; Impact: Read Application Data — By causing the wrong code to be invoked, the attacker might be able to trigger a runtime error that leaks sensitive information in the error message, such as CWE-536.

## Potential Mitigations
- [Architecture and Design] Refactor your code to avoid using reflection.
- [Architecture and Design] Do not use user-controlled inputs to select and load classes or code.
- [Implementation] Apply strict input validation by using allowlists or indirect selection to ensure that the user is only selecting allowable classes or code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- A common reason that programmers use the reflection API is to implement their own command dispatcher. The following example shows a command dispatcher that does not use reflection:
