# CAPEC-640: Inclusion of Code in Existing Process

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/640.html  

## Description
The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute arbitrary code in the address space of a separate live process. The adversary could use running code in the context of another process to try to access process's memory, system/network resources, etc. The goal of this attack is to evade detection defenses and escalate privileges by masking the malicious code under an existing legitimate process. Examples of approaches include but not limited to: dynamic-link library (DLL) injection, portable executable injection, thread execution hijacking, ptrace system calls, VDSO hijacking, function hooking, reflective code loading, and more.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted application fails to verify the integrity of the running process that allows an adversary to execute arbitrary code.

## Skills Required
- [High] Knowledge of how to load malicious code into the memory space of a running process, as well as the ability to have the running process execute this code. For example, with DLL injection, the adversary must know how to load a DLL into the memory space of another running process, and cause this process to execute the code inside of the DLL.

## Consequences
- Scope: Integrity, Confidentiality; Impact: Execute Unauthorized Commands, Read Data

## Mitigations
- Prevent unknown or malicious software from loading through using an allowlist policy.
- Properly restrict the location of the software being used.
- Leverage security kernel modules providing advanced access control and process restrictions like SELinux.
- Monitor API calls like CreateRemoteThread, SuspendThread/SetThreadContext/ResumeThread, QueueUserAPC, and similar for Windows.
- Monitor API calls like ptrace system call, use of LD_PRELOAD environment variable, dlfcn dynamic linking API calls, and similar for Linux.
- Monitor API calls like SetWindowsHookEx and SetWinEventHook which install hook procedures for Windows.
- Monitor processes and command-line arguments for unknown behavior related to code injection.

## Related Weaknesses (CWE)
- CWE-114
- CWE-829
