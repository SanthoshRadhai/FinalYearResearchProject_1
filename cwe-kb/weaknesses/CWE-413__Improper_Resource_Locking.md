# CWE-413: Improper Resource Locking

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/413.html  

## Description
The product does not lock or does not correctly lock a resource when the product must have exclusive access to the resource.

## Extended Description
When a resource is not properly locked, an attacker could modify the resource while it is being operated on by the product. This might violate the product's assumption that the resource will not change, potentially leading to unexpected behaviors.

## Related Weaknesses
- ChildOf: CWE-667

## Common Consequences
- Scope: Integrity, Availability; Impact: Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart

## Potential Mitigations
- [Architecture and Design] Use a non-conflicting privilege scheme.
- [Architecture and Design, Implementation] Use synchronization when locking a resource.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following function attempts to acquire a lock in order to perform operations on a shared resource.
- This Java example shows a simple BankAccount class with deposit and withdraw methods.
