# CWE-1342: Information Exposure through Microarchitectural State after Transient Execution

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1342.html  

## Description
The processor does not properly clear microarchitectural state after incorrect microcode assists or speculative execution, resulting in transient execution.

## Extended Description
In many processor architectures an exception, mis-speculation, or microcode assist results in a flush operation to clear results that are no longer required. This action prevents these results from influencing architectural state that is intended to be visible from software. However, traces of this transient execution may remain in microarchitectural buffers, resulting in a change in microarchitectural state that can expose sensitive information to an attacker using side-channel analysis. For example, Load Value Injection (LVI) [REF-1202] can exploit direct injection of erroneous values into intermediate load and store buffers. Several conditions may need to be fulfilled for a successful attack: incorrect transient execution that results in remanence of sensitive information; attacker has the ability to provoke microarchitectural exceptions; operations and structures in victim code that can be exploited must be identified.

## Related Weaknesses
- ChildOf: CWE-226
- ChildOf: CWE-226

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Modify Memory, Read Memory, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design, Requirements] Hardware ensures that no illegal data flows from faulting micro-ops exists at the microarchitectural level.
- [Build and Compilation] Include instructions that explicitly remove traces of unneeded computations from software interactions with microarchitectural elements e.g. lfence, sfence, mfence, clflush.

## Demonstrative Examples (summary)
- Faulting loads in a victim domain may trigger incorrect transient forwarding, which leaves secret-dependent traces in the microarchitectural state. Consider this example from [REF-1203].
