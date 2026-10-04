# CWE-571: Expression is Always True

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/571.html  

## Description
The product contains an expression that will always evaluate to true.

## Related Weaknesses
- ChildOf: CWE-710
- CanPrecede: CWE-561

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Potential Mitigations
- [Implementation] Consider refactoring the code, or determine if the code is not including a condition that could cause the expression to become false.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java example the updateInventory() method used within an e-business product ordering/inventory application will check if the input product number is in the store or in the warehouse. If the product is found, the method will update the store or warehouse database as well as the aggregate product database. If the product is not found, the method intends to do some special processing without updating any database.
