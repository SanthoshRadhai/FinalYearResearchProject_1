# CWE-191: Integer Underflow (Wrap or Wraparound)

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/191.html  

## Description
The product subtracts one value from another, such that the result is less than the minimum allowable integer value, which produces a value that is not equal to the correct result.

## Extended Description
This can happen in signed and unsigned cases.

## Related Weaknesses
- ChildOf: CWE-682
- ChildOf: CWE-682

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Instability — This weakness will generally lead to undefined behavior and therefore crashes. In the case of overflows involving loop index variables, the likelihood of infinite loops is also high.
- Scope: Integrity; Impact: Modify Memory — If the value in question is important to data (as opposed to flow), simple data corruption has occurred. Also, if the wrap around results in other conditions such as buffer overflows, further memory corruption may occur.
- Scope: Confidentiality, Availability, Access Control; Impact: Execute Unauthorized Code or Commands, Bypass Protection Mechanism — This weakness can sometimes trigger buffer overflows which can be used to execute arbitrary code. This is usually outside the scope of a program's implicit security policy.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example subtracts from a 32 bit signed integer.
- This code performs a stack allocation based on a length calculation.
