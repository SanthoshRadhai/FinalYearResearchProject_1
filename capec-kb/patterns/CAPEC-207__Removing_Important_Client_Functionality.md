# CAPEC-207: Removing Important Client Functionality

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/207.html  

## Description
An adversary removes or disables functionality on the client that the server assumes to be present and trustworthy.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- The targeted server must assume the client performs important actions to protect the server or the server functionality. For example, the server may assume the client filters outbound traffic or that the client performs all price calculations correctly. Moreover, the server must fail to detect when these assumptions are violated by a client.

## Skills Required
- [High] To reverse engineer the client-side code to disable/remove the functionality on the client that the server relies on.
- [Low] The adversary installs a web tool that allows scripts or the DOM model of web-based applications to be modified before they are executed in a browser. GreaseMonkey and Firebug are two examples of such tools.

## Resources Required
- The adversary must have access to a client and be able to modify the client behavior, often through reverse engineering. If the server is assuming specific client functionality, this usually means the server only recognizes a specific client application, rather than a broad class of client applications. Reverse engineering tools would likely be necessary.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.
- Design: Ship client-side application with integrity checks (code signing) when possible.
- Design: Use obfuscation and other techniques to prevent reverse engineering the client code.

## Related Weaknesses (CWE)
- CWE-602
