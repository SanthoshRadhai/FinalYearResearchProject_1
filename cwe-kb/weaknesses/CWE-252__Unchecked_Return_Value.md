# CWE-252: Unchecked Return Value

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/252.html  

## Description
The product does not check the return value from a method or function, which can prevent it from detecting unexpected states and conditions.

## Extended Description
Two common programmer assumptions are "this function call can never fail" and "it doesn't matter if this function call fails". If an attacker can force the function to fail or otherwise return a value that is not expected, then the subsequent program logic could lead to a vulnerability, because the product is not in a state that the programmer assumes. For example, if the program calls a function to drop privileges but does not check the return code to ensure that privileges were successfully dropped, then the program will continue to operate with the higher privileges.

## Related Weaknesses
- ChildOf: CWE-754
- ChildOf: CWE-754
- CanPrecede: CWE-476

## Common Consequences
- Scope: Availability, Integrity; Impact: Unexpected State, DoS: Crash, Exit, or Restart — An unexpected return value could place the system in a state that could lead to a crash or other unintended behaviors.

## Potential Mitigations
- [Implementation] Check the results of all functions that return a value and verify that the value is expected.
- [Implementation] For any pointers that could have been modified or provided from a function that can return NULL, check the pointer for NULL before use. When working with a multithreaded or otherwise asynchronous environment, ensure that proper locking APIs are used to lock before the check, and unlock when it has finished [REF-1484].
- [Implementation] Ensure that you account for all possible return values from the function.
- [Implementation] When designing a function, make sure you return a value or throw an exception in case of an error.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Consider the following code segment:
- In the following example, it is possible to request that memcpy move a much larger segment of memory than assumed:
- The following code does not check to see if memory allocation succeeded before attempting to use the pointer returned by malloc().
- The following examples read a file into a byte array.
- The following code does not check to see if the string returned by getParameter() is null before calling the member function compareTo(), potentially causing a NULL dereference.
- The following code shows a system property that is set to null and later dereferenced by a programmer who mistakenly assumes it will always be defined.
- The following VB.NET code does not check to make sure that it has read 50 bytes from myfile.txt. This can cause DoDangerousOperation() to operate on an unexpected value.
- It is not uncommon for Java programmers to misunderstand read() and related methods that are part of many java.io classes. Most errors and unusual events in Java result in an exception being thrown. But the stream and reader classes do not consider it unusual or exceptional if only a small amount of data becomes available. These classes simply add the small amount of data to the return buffer, and set the return value to the number of bytes or characters read. There is no guarantee that the amount of data returned is equal to the amount of data requested. This behavior makes it important for programmers to examine the return value from read() and other IO methods to ensure that they receive the amount of data they expect.
- This example takes an IP address from a user, verifies that it is well formed and then looks up the hostname and copies it into a buffer.
- The following function attempts to acquire a lock in order to perform operations on a shared resource.
