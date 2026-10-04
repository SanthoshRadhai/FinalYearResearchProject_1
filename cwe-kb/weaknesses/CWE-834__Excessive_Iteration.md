# CWE-834: Excessive Iteration

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/834.html  

## Description
The product performs an iteration or loop without sufficiently limiting the number of times that the loop is executed.

## Extended Description
If the iteration can be influenced by an attacker, this weakness could allow attackers to consume excessive resources such as CPU or memory. In many cases, a loop does not need to be infinite in order to cause enough resource consumption to adversely affect the product or its host system; it depends on the amount of resources consumed per iteration.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Amplification, DoS: Crash, Exit, or Restart — Excessive looping will cause unexpected consumption of resources, such as CPU cycles or memory. The product's operation may slow down, or cause a long time to respond. If limited resources such as memory are consumed for each iteration, the loop may eventually cause a crash or program exit due to exhaustion of resources, such as an out-of-memory error.

## Detection Methods
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Fuzz Tester Framework-based Fuzzer Forced Path Execution
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Context-configured Source Code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- In this example a mistake exists in the code where the exit condition contained in flg is never called. This results in the function calling itself over and over again until the stack is exhausted.
- For this example, the method isReorderNeeded is part of a bookstore application that determines if a particular book needs to be reordered based on the current inventory count and the rate at which the book is being sold.
