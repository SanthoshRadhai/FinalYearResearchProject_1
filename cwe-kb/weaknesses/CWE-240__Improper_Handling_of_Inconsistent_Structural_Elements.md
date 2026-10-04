# CWE-240: Improper Handling of Inconsistent Structural Elements

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/240.html  

## Description
The product does not handle or incorrectly handles when two or more structural elements should be consistent, but are not.

## Related Weaknesses
- ChildOf: CWE-237
- ChildOf: CWE-707

## Common Consequences
- Scope: Integrity, Other; Impact: Varies by Context, Unexpected State

## Demonstrative Examples (summary)
- In the following C/C++ example the method processMessageFromSocket() will get a message from a socket, placed into a buffer, and will parse the contents of the buffer into a structure that contains the message length and the message body. A for loop is used to copy the message body into a local character string which will be passed to another method for processing.
