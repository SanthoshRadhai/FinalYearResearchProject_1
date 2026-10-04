# CWE-197: Numeric Truncation Error

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/197.html  

## Description
Truncation errors occur when a primitive is cast to a primitive of a smaller size and data is lost in the conversion.

## Extended Description
When a primitive is cast to a smaller primitive, the high order bits of the large value are lost in the conversion, potentially resulting in an unexpected value that is not equal to the original value. This value may be required as an index into a buffer, a loop iterator, or simply necessary state data. In any case, the value cannot be trusted and the system will be in an undefined state. While this method may be employed viably to isolate the low bits of a value, this usage is rare, and truncation usually implies that an implementation error has occurred.

## Related Weaknesses
- ChildOf: CWE-681
- ChildOf: CWE-681
- ChildOf: CWE-681
- CanAlsoBe: CWE-195
- CanAlsoBe: CWE-196
- CanAlsoBe: CWE-192
- CanAlsoBe: CWE-194

## Common Consequences
- Scope: Integrity; Impact: Modify Memory — The true value of the data is lost and corrupted data is used.

## Potential Mitigations
- [Implementation] Ensure that no casts, implicit or explicit, take place that move from a larger size primitive or a smaller size primitive.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example, while not exploitable, shows the possible mangling of values associated with truncation errors:
- In the following Java example, the method updateSalesForProduct is part of a business application class that updates the sales information for a particular product. The method receives as arguments the product ID and the integer amount sold. The product ID is used to retrieve the total product count from an inventory object which returns the count as an integer. Before calling the method of the sales object to update the sales count the integer values are converted to The primitive type short since the method requires short type for the method arguments.
