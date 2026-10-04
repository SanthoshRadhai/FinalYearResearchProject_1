# CAPEC-237: Escaping a Sandbox by Calling Code in Another Language

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/237.html  

## Description
The attacker may submit malicious code of another language to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. For instance, Java code cannot perform unsafe operations, such as modifying arbitrary memory locations, due to restrictions placed on it by the Byte code Verifier and the JVM. If allowed, Java code can call directly into native C code, which may perform unsafe operations, such as call system calls and modify arbitrary memory locations on their behalf. To provide isolation, Java does not grant untrusted code with unmediated access to native C code. Instead, the sandboxed code is typically allowed to call some subset of the pre-existing native code that is part of standard libraries.

## Related Attack Patterns
- ChildOf: CAPEC-480

## Skills Required
- [High] The attacker must have a good knowledge of the platform specific mechanisms of signing and verifying code. Most code signing and verification schemes are based on use of cryptography, the attacker needs to have an understand of these cryptographic operations in good detail.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges

## Mitigations
- Assurance: Sanitize the code of the standard libraries to make sure there is no security weaknesses in them.
- Design: Use obfuscation and other techniques to prevent reverse engineering the standard libraries.
- Assurance: Use static analysis tool to do code review and dynamic tool to do penetration test on the standard library.
- Configuration: Get latest updates for the computer.

## Related Weaknesses (CWE)
- CWE-693
