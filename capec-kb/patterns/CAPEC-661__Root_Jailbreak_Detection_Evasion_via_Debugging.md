# CAPEC-661: Root/Jailbreak Detection Evasion via Debugging

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/661.html  

## Description
An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Rooting/Jailbreaking a mobile device also provides users with access to system debuggers and disassemblers, which can be leveraged to exploit applications by dumping the application's memory at runtime in order to remove or bypass signature verification methods. This further allows the adversary to evade Root/Jailbreak detection mechanisms, which can result in execution of administrative commands, obtaining confidential data, impersonating legitimate users of the application, and more.

## Related Attack Patterns
- ChildOf: CAPEC-121
- CanPrecede: CAPEC-68
- CanPrecede: CAPEC-660

## Prerequisites
- A debugger must be able to be inserted into the targeted application.

## Skills Required
- [High] Knowledge about Root/Jailbreak detection and evasion techniques.
- [Medium] Knowledge about runtime debugging.

## Resources Required
- The adversary must have a Rooted/Jailbroken mobile device with debugging capabilities.

## Consequences
- Scope: Integrity, Authorization; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Instantiate checks within the application code that ensures debuggers are not attached.

## Related Weaknesses (CWE)
- CWE-489
