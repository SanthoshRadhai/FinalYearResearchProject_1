# CWE-835: Loop with Unreachable Exit Condition ('Infinite Loop')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/835.html  

## Description
The product contains an iteration or loop with an exit condition that cannot be reached, i.e., an infinite loop.

## Related Weaknesses
- ChildOf: CWE-834
- ChildOf: CWE-834

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Amplification — An infinite loop will cause unexpected consumption of resources, such as CPU cycles or memory. The software's operation may slow down, or cause a long time to respond.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code the method processMessagesFromServer attempts to establish a connection to a server and read and process messages from the server. The method uses a do/while loop to continue trying to establish the connection to the server when an attempt fails.
- For this example, the method isReorderNeeded is part of a bookstore application that determines if a particular book needs to be reordered based on the current inventory count and the rate at which the book is being sold.
