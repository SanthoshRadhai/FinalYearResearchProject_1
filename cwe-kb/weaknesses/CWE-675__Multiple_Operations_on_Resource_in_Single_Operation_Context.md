# CWE-675: Multiple Operations on Resource in Single-Operation Context

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/675.html  

## Description
The product performs the same operation on a resource two or more times, when the operation should only be applied once.

## Related Weaknesses
- ChildOf: CWE-573
- PeerOf: CWE-586
- PeerOf: CWE-102

## Common Consequences
- Scope: Other; Impact: Other

## Demonstrative Examples (summary)
- The following code shows a simple example of a double free vulnerability.
- This code binds a server socket to port 21, allowing the server to listen for traffic on that port.
