# CAPEC-123: Buffer Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/123.html  

## Description
An adversary manipulates an application's interaction with a buffer in an attempt to read or modify data they shouldn't have access to. Buffer attacks are distinguished in that it is the buffer space itself that is the target of the attack rather than any code responsible for interpreting the content of the buffer. In virtually all buffer attacks the content that is placed in the buffer is immaterial. Instead, most buffer attacks involve retrieving or providing more input than can be stored in the allocated buffer, resulting in the reading or overwriting of other unintended program memory.

## Prerequisites
- The adversary must identify a programmatic means for interacting with a buffer, such as vulnerable C code, and be able to provide input to this interaction.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Execute Unauthorized Commands, Modify Data, Read Data

## Mitigations
- To help protect an application from buffer manipulation attacks, a number of potential mitigations can be leveraged. Before starting the development of the application, consider using a code language (e.g., Java) or compiler that limits the ability of developers to act beyond the bounds of a buffer. If the chosen language is susceptible to buffer related issues (e.g., C) then consider using secure functions instead of those vulnerable to buffer manipulations. If a potentially dangerous function must be used, make sure that proper boundary checking is performed. Additionally, there are often a number of compiler-based mechanisms (e.g., StackGuard, ProPolice and the Microsoft Visual Studio /GS flag) that can help identify and protect against potential buffer issues. Finally, there may be operating system level preventative functionality that can be applied.

## Related Weaknesses (CWE)
- CWE-119
