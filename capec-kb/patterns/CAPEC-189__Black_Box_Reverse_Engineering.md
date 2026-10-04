# CAPEC-189: Black Box Reverse Engineering

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/189.html  

## Description
An adversary discovers the structure, function, and composition of a type of computer software through black box analysis techniques. 'Black Box' methods involve interacting with the software indirectly, in the absence of direct access to the executable object. Such analysis typically involves interacting with the software at the boundaries of where the software interfaces with a larger execution environment, such as input-output vectors, libraries, or APIs. Black Box Reverse Engineering also refers to gathering physical side effects of a hardware device, such as electromagnetic radiation or sounds.

## Related Attack Patterns
- ChildOf: CAPEC-188

## Resources Required
- Black box methods require (at minimum) the ability to interact with the functional boundaries where the software communicates with a larger processing environment, such as inter-process communication on a host operating system, or via networking protocols.

## Related Weaknesses (CWE)
- CWE-203
- CWE-1255
- CWE-1300
