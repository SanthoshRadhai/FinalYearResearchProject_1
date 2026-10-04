# CWE-581: Object Model Violation: Just One of Equals and Hashcode Defined

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/581.html  

## Description
The product does not maintain equal hashcodes for equal objects.

## Extended Description
Java objects are expected to obey a number of invariants related to equality. One of these invariants is that equal objects must have equal hashcodes. In other words, if a.equals(b) == true then a.hashCode() == b.hashCode().

## Related Weaknesses
- ChildOf: CWE-573
- ChildOf: CWE-697

## Common Consequences
- Scope: Integrity, Other; Impact: Other — If this invariant is not upheld, it is likely to cause trouble if objects of this class are stored in a collection. If the objects of the class in question are used as a key in a Hashtable or if they are inserted into a Map or Set, it is critical that equal objects have equal hashcodes.

## Potential Mitigations
- [Implementation] Both Equals() and Hashcode() should be defined.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
