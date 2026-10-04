# CWE-1321: Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1321.html  

## Description
The product receives input from an upstream component that specifies attributes that are to be initialized or updated in an object, but it does not properly control modifications of attributes of the object prototype.

## Related Weaknesses
- ChildOf: CWE-915
- ChildOf: CWE-913
- CanPrecede: CWE-471

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Read Application Data, Modify Application Data — This weakness is usually exploited by using a special attribute of objects called proto, constructor, or prototype. Such attributes give access to the object prototype. An attacker can inject attributes that are used in other components by adding or modifying attributes of an object prototype. This creates attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the product depends on existence or non-existence of certain attributes, or uses pre-defined attributes of the object prototype (such as hasOwnProperty, toString, or valueOf).
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — An attacker can override existing attributes with ones that have incompatible type, which may lead to a crash.

## Potential Mitigations
- [Implementation] By freezing the object prototype first (for example, Object.freeze(Object.prototype)), modification of the prototype becomes impossible.
- [Architecture and Design] By blocking modifications of attributes that resolve to object prototype, such as proto or prototype, this weakness can be mitigated.
- [Implementation] When handling untrusted objects, validating using a schema can be used.
- [Implementation] By using an object without prototypes (via Object.create(null) ), adding object prototype attributes by accessing the prototype via the special attributes becomes impossible, mitigating this weakness.
- [Implementation] Map can be used instead of objects in most cases. If Map methods are used instead of object attributes, it is not possible to access the object prototype or modify it.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This function sets object attributes based on a dot-separated path.
