# CWE-126: Buffer Over-read

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/126.html  

## Description
The product reads from a buffer using buffer access mechanisms such as indexes or pointers that reference memory locations after the targeted buffer.

## Related Weaknesses
- ChildOf: CWE-125
- ChildOf: CWE-788

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory
- Scope: Confidentiality; Impact: Bypass Protection Mechanism — By reading out-of-bounds memory, an attacker might be able to get secret values, such as memory addresses, which can bypass protection mechanisms such as ASLR in order to improve the reliability and likelihood of exploiting a separate weakness to achieve code execution instead of just denial of service.
- Scope: Availability, Integrity; Impact: DoS: Crash, Exit, or Restart — An attacker might be able to cause a crash or other denial of service by causing the product to read a memory location that is not allowed (such as a segmentation fault), or to cause other conditions in which the read operation returns more data than is expected.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- In the following C/C++ example the method processMessageFromSocket() will get a message from a socket, placed into a buffer, and will parse the contents of the buffer into a structure that contains the message length and the message body. A for loop is used to copy the message body into a local character string which will be passed to another method for processing.
- The following C/C++ example demonstrates a buffer over-read due to a missing NULL terminator. The main method of a pattern matching utility that looks for a specific pattern within a specific file uses the string strncopy() method to copy the command line user input file name and pattern to the Filename and Pattern character arrays respectively.
