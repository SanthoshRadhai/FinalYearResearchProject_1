# CAPEC-660: Root/Jailbreak Detection Evasion via Hooking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/660.html  

## Description
An adversary forces a non-restricted mobile application to load arbitrary code or code files, via Hooking, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Adversaries may further leverage these capabilities to escalate privileges or bypass access control on legitimate applications. Although many mobile applications check if a mobile device is Rooted/Jailbroken prior to authorized use of the application, adversaries may be able to "hook" code in order to circumvent these checks. Successfully evading Root/Jailbreak detection allows an adversary to execute administrative commands, obtain confidential data, impersonate legitimate users of the application, and more.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted application must be non-restricted to allow code hooking.

## Skills Required
- [High] Knowledge about Root/Jailbreak detection and evasion techniques.
- [Medium] Knowledge about code hooking.

## Resources Required
- The adversary must have a Rooted/Jailbroken mobile device.
- The adversary needs to have enough access to the target application to control the included code or file.

## Consequences
- Scope: Integrity, Authorization; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Ensure mobile applications are signed appropriately to avoid code inclusion via hooking.
- Inspect the application's memory for suspicious artifacts, such as shared objects/JARs or dylibs, after other Root/Jailbreak detection methods.
- Inspect the application's stack trace for suspicious method calls.
- Allow legitimate native methods, and check for non-allowed native methods during Root/Jailbreak detection methods.
- For iOS applications, ensure application methods do not originate from outside of Apple's SDK.

## Related Weaknesses (CWE)
- CWE-829
