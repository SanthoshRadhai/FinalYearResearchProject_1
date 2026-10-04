# CWE-674: Uncontrolled Recursion

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/674.html  

## Description
The product does not properly control the amount of recursion that takes place, consuming excessive resources, such as allocated memory or the program stack.

## Related Weaknesses
- ChildOf: CWE-834

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — Resources including CPU, memory, and stack memory could be rapidly consumed or exhausted, eventually leading to an exit or crash.
- Scope: Confidentiality; Impact: Read Application Data — In some cases, an application's interpreter might kill a process or thread that appears to be consuming too much resources, such as with PHP's memory_limit setting. When the interpreter kills the process/thread, it might report an error containing detailed information such as the application's installation path.

## Potential Mitigations
- [Implementation] Ensure that an end condition will be reached under all logic conditions. The end condition may include checking against the depth of recursion and exiting with an error if the recursion goes too deep. The complexity of the end condition contributes to the effectiveness of this action.
- [Implementation] Increase the stack size.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example a mistake exists in the code where the exit condition contained in flg is never called. This results in the function calling itself over and over again until the stack is exhausted.
