# CWE-456: Missing Initialization of a Variable

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/456.html  

## Description
The product does not initialize critical variables, which causes the execution environment to use unexpected values.

## Related Weaknesses
- ChildOf: CWE-909
- ChildOf: CWE-665
- ChildOf: CWE-665
- CanPrecede: CWE-89
- CanPrecede: CWE-120
- CanPrecede: CWE-98
- CanPrecede: CWE-457

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Quality Degradation, Varies by Context — The uninitialized data may be invalid, causing logic errors within the program. In some cases, this could result in a security problem.

## Potential Mitigations
- [Implementation] Ensure that critical variables are initialized before first use [REF-1485].
- [Requirements] Choose a language that is not susceptible to these issues.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This function attempts to extract a pair of numbers from a user-supplied string.
- Here, an uninitialized field in a Java class is used in a seldom-called method, which would cause a NullPointerException to be thrown.
- This code first authenticates a user, then allows a delete command if the user is an administrator.
- In the following Java code the BankManager class uses the user variable of the class User to allow authorized users to perform bank manager tasks. The user variable is initialized within the method setUser that retrieves the User from the User database. The user is then authenticated as unauthorized user through the method authenticateUser.
- This example will leave test_string in an unknown condition when i is the same value as err_val, because test_string is not initialized (CWE-456). Depending on where this code segment appears (e.g. within a function body), test_string might be random if it is stored on the heap or stack. If the variable is declared in static memory, it might be zero or NULL. Compiler optimization might contribute to the unpredictability of this address.
- Consider the following merchant server application as implemented in [REF-1475]. It receives card payment information (orderPgData instance in OrderPgData.java) from the payment gateway (such as PayPal). The next step is to complete the payment (finalizeOrder() in Main.java). The merchant server validates the amount (validateAmount() in OrderPgData.java), and if the validation is successful, then the payment is completed.
