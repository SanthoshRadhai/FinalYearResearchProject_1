# CAPEC-641: DLL Side-Loading

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/641.html  

## Description
An adversary places a malicious version of a Dynamic-Link Library (DLL) in the Windows Side-by-Side (WinSxS) directory to trick the operating system into loading this malicious DLL instead of a legitimate DLL. Programs specify the location of the DLLs to load via the use of WinSxS manifests or DLL redirection and if they aren't used then Windows searches in a predefined set of directories to locate the file. If the applications improperly specify a required DLL or WinSxS manifests aren't explicit about the characteristics of the DLL to be loaded, they can be vulnerable to side-loading.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The target must fail to verify the integrity of the DLL before using them.

## Skills Required
- [High] Trick the operating system in loading a malicious DLL instead of a legitimate DLL.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands, Bypass Protection Mechanism

## Mitigations
- Prevent unknown DLLs from loading through using an allowlist policy.
- Patch installed applications as soon as new updates become available.
- Properly restrict the location of the software being used.
- Use of sxstrace.exe on Windows as well as manual inspection of the manifests.
- Require code signing and avoid using relative paths for resources.

## Related Weaknesses (CWE)
- CWE-706
