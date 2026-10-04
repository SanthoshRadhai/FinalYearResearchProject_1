# CWE-839: Numeric Range Comparison Without Minimum Check

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/839.html  

## Description
The product checks a value to ensure that it is less than or equal to a maximum, but it does not also verify that the value is greater than or equal to the minimum.

## Extended Description
Some products use signed integers or floats even when their values are only expected to be positive or 0. An input validation check might assume that the value is positive, and only check for the maximum value. If the value is negative, but the code assumes that the value is positive, this can produce an error. The error may have security consequences if the negative value is used for memory allocation, array access, buffer access, etc. Ultimately, the error could lead to a buffer overflow or other type of memory corruption. The use of a negative number in a positive-only context could have security implications for other types of resources. For example, a shopping cart might check that the user is not requesting more than 10 items, but a request for -3 items could cause the application to calculate a negative price and credit the attacker's account.

## Related Weaknesses
- ChildOf: CWE-1023
- CanPrecede: CWE-195
- CanPrecede: CWE-682
- CanPrecede: CWE-119
- CanPrecede: CWE-124

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Application Data, Execute Unauthorized Code or Commands — An attacker could modify the structure of the message or data being sent to the downstream component, possibly injecting commands.
- Scope: Availability; Impact: DoS: Resource Consumption (Other) — in some contexts, a negative value could lead to resource consumption.
- Scope: Confidentiality, Integrity; Impact: Modify Memory, Read Memory — If a negative value is used to access memory, buffers, or other indexable structures, it could access memory outside the bounds of the buffer.

## Potential Mitigations
- [Implementation] If the number to be used is always expected to be positive, change the variable type from signed to unsigned or size_t.
- [Implementation] If the number to be used could have a negative value based on the specification (thus requiring a signed value), but the number should only be positive to preserve code correctness, then include a check to ensure that the value is positive.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code is intended to read an incoming packet from a socket and extract one or more headers.
- The following code reads a maximum size and performs a sanity check on that size. It then performs a strncpy, assuming it will not exceed the boundaries of the array. While the use of "short s" is forced in this particular example, short int's are frequently used within real-world code, such as code that processes structured data.
- In the following code, the method retrieves a value from an array at a specific array index location that is given as an input parameter to the method
- The following code shows a simple BankAccount class with deposit and withdraw methods.
