# CAPEC-44: Overflow Binary Resource File

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/44.html  

## Description
An attack of this type exploits a buffer overflow vulnerability in the handling of binary resources. Binary resources may include music files like MP3, image files like JPEG files, and any other binary file. These attacks may pass unnoticed to the client machine through normal usage of files, such as a browser loading a seemingly innocent JPEG file. This can allow the adversary access to the execution stack and execute arbitrary code in the target process.

## Related Attack Patterns
- ChildOf: CAPEC-100
- ChildOf: CAPEC-23

## Prerequisites
- Target software processes binary resource files.
- Target software contains a buffer overflow vulnerability reachable through input from a user-controllable binary resource file.

## Skills Required
- [Medium] To modify file, deceive client into downloading, locate and exploit remote stack or heap vulnerability

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Perform appropriate bounds checking on all buffers.
- Design: Enforce principle of least privilege
- Design: Static code analysis
- Implementation: Execute program in less trusted process space environment, do not allow lower integrity processes to write to higher integrity processes
- Implementation: Keep software patched to ensure that known vulnerabilities are not available for adversaries to target on host.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-697
