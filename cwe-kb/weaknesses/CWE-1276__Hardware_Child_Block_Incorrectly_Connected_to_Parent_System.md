# CWE-1276: Hardware Child Block Incorrectly Connected to Parent System

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1276.html  

## Description
Signals between a hardware IP and the parent system design are incorrectly connected causing security risks.

## Extended Description
Individual hardware IP must communicate with the parent system in order for the product to function correctly and as intended. If implemented incorrectly, while not causing any apparent functional issues, may cause security issues. For example, if the IP should only be reset by a system-wide hard reset, but instead the reset input is connected to a software-triggered debug mode reset (which is also asserted during a hard reset), integrity of data inside the IP can be violated.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Varies by Context

## Potential Mitigations
- [Testing] System-level verification may be used to ensure that components are correctly connected and that design security requirements are not violated due to interactions between various IP blocks.

## Demonstrative Examples (summary)
- Many SoCs use hardware to partition system resources between trusted and untrusted entities. One example of this concept is the Arm TrustZone, in which the processor and all security-aware IP attempt to isolate resources based on the status of a privilege bit. This privilege bit is part of the input interface in all TrustZone-aware IP. If this privilege bit is accidentally grounded or left unconnected when the IP is instantiated, privilege escalation of all input data may occur.
- Here is a code snippet from the Ariane core module in the HACK@DAC'21 Openpiton SoC [REF-1362]. To ensure full functional correctness, developers connect the ports with names. However, in some cases developers forget to connect some of these ports to the desired signals in the parent module. These mistakes by developers can lead to incorrect functional behavior or, in some cases, introduce security vulnerabilities.
