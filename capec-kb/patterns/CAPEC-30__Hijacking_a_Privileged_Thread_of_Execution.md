# CAPEC-30: Hijacking a Privileged Thread of Execution

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/30.html  

## Description
An adversary hijacks a privileged thread of execution by injecting malicious code into a running process. By using a privleged thread to do their bidding, adversaries can evade process-based detection that would stop an attack that creates a new process. This can lead to an adversary gaining access to the process's memory and can also enable elevated privileges. The most common way to perform this attack is by suspending an existing thread and manipulating its memory.

## Related Attack Patterns
- ChildOf: CAPEC-233

## Prerequisites
- The application in question employs a threaded model of execution with the threads operating at, or having the ability to switch to, a higher privilege level than normal users
- In order to feasibly execute this class of attacks, the adversary must have the ability to hijack a privileged thread. This ability includes, but is not limited to, modifying environment variables that affect the process the thread belongs to, or calling native OS calls that can suspend and alter process memory. This does not preclude network-based attacks, but makes them conceptually more difficult to identify and execute.

## Skills Required
- [High] Hijacking a thread involves knowledge of how processes and threads function on the target platform, the design of the target application as well as the ability to identify the primitives to be used or manipulated to hijack the thread.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The adversary needs to be able to latch onto a privileged thread. The adversary does, however, need to be able to program, compile, and link to the victim binaries being executed so that it will turn control of a privileged thread over to the adversary's malicious code. This is the case even if the adversary conducts the attack remotely.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.
- Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.

## Related Weaknesses (CWE)
- CWE-270
