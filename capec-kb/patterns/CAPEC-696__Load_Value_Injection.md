# CAPEC-696: Load Value Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/696.html  

## Description
An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution in which a faulting or assisted load instruction transiently forwards adversary-controlled data from microarchitectural buffers. By inducing a page fault or microcode assist during victim execution, an adversary can force legitimate victim execution to operate on the adversary-controlled data which is stored in the microarchitectural buffers. The adversary can then use existing code gadgets and side channel analysis to discover victim secrets that have not yet been flushed from microarchitectural state or hijack the system control flow.

## Related Attack Patterns
- ChildOf: CAPEC-663

## Prerequisites
- The adversary needs at least user execution access to a system and a maliciously crafted program/application/process with unprivileged code to misuse transient instruction set execution of the CPU.
- The CPU incorrectly transiently forwards values from microarchitectural buffers after faulting or assisted loads
- The adversary needs the ability to induce page faults or microcode assists on the target system.
- Code gadgets exist that allow the adversary to hijack transient execution and encode secrets into the microarchitectural state.

## Skills Required
- [High] Detailed knowledge on how various CPU architectures and microcode perform transient execution for various low-level assembly language code instructions/operations.
- [High] Detailed knowledge on compiled binaries and operating system shared libraries of instruction sequences, and layout of application and OS/Kernel address spaces for data leakage.
- [High] The ability to provoke faulting or assisted loads in legitimate execution.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Do not allow the forwarding of data resulting from a faulting or assisted instruction. Some current mitigations claim to zero out the forwarded data, but this mitigation still does not suffice.
- Insert explicit “lfence” speculation barriers in software before potentially faulting or assisted loads. This halts transient execution until all previous instructions have been executed and ensures that the architecturally correct value is forwarded.

## Related Weaknesses (CWE)
- CWE-1342
