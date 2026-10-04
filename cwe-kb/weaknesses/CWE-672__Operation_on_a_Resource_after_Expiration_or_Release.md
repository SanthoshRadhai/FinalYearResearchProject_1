# CWE-672: Operation on a Resource after Expiration or Release

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/672.html  

## Description
The product uses, accesses, or otherwise operates on a resource after that resource has been expired, released, or revoked.

## Related Weaknesses
- ChildOf: CWE-666

## Common Consequences
- Scope: Integrity, Confidentiality; Impact: Modify Application Data, Read Application Data — If a released resource is subsequently reused or reallocated, then an attempt to use the original resource might allow access to sensitive data that is associated with a different user or entity.
- Scope: Other, Availability; Impact: Other, DoS: Crash, Exit, or Restart — When a resource is released it might not be in an expected state, later attempts to access the resource may lead to resultant errors that may lead to a crash.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code shows a simple example of a use after free error:
- The following code shows a simple example of a double free error:
- In the following C/C++ example the method processMessage is used to process a message received in the input array of char arrays. The input message array contains two char arrays: the first is the length of the message and the second is the body of the message. The length of the message is retrieved and used to allocate enough memory for a local char array, messageBody, to be created for the message body. The messageBody is processed in the method processMessageBody that will return an error if an error occurs while processing. If an error occurs then the return result variable is set to indicate an error and the messageBody char array memory is released using the method free and an error message is sent to the logError method.
