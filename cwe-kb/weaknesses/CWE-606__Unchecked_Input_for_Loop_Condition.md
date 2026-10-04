# CWE-606: Unchecked Input for Loop Condition

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/606.html  

## Description
The product does not properly check inputs that are used for loop conditions, potentially leading to a denial of service or other consequences because of excessive looping.

## Related Weaknesses
- ChildOf: CWE-1284
- CanPrecede: CWE-834

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU)

## Potential Mitigations
- [Implementation] Do not use user-controlled data for loop conditions.
- [Implementation] Perform input validation.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
- In the following C/C++ example the method processMessageFromSocket() will get a message from a socket, placed into a buffer, and will parse the contents of the buffer into a structure that contains the message length and the message body. A for loop is used to copy the message body into a local character string which will be passed to another method for processing.
