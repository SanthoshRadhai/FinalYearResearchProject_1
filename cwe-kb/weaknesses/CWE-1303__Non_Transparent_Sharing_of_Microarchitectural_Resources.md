# CWE-1303: Non-Transparent Sharing of Microarchitectural Resources

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1303.html  

## Description
Hardware structures shared across execution contexts (e.g., caches and branch predictors) can violate the expected architecture isolation between contexts.

## Extended Description
Modern processors use techniques such as out-of-order execution, speculation, prefetching, data forwarding, and caching to increase performance. Details about the implementation of these techniques are hidden from the programmer's view. This is problematic when the hardware implementation of these techniques results in resources being shared across supposedly isolated contexts. Contention for shared resources between different contexts opens covert channels that allow malicious programs executing in one context to recover information from another context. Some examples of shared micro-architectural resources that have been used to leak information between contexts are caches, branch prediction logic, and load or store buffers. Speculative and out-of-order execution provides an attacker with increased control over which data is leaked through the covert channel. If the extent of resource sharing between contexts in the design microarchitecture is undocumented, it is extremely difficult to ensure system assets are protected against disclosure.

## Related Weaknesses
- ChildOf: CWE-1189
- ChildOf: CWE-203

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data, Read Memory — Microarchitectural side-channels have been used to leak specific information such as cryptographic keys, and Address Space Layout Randomization (ALSR) offsets as well as arbitrary memory.

## Potential Mitigations
- [Architecture and Design] Microarchitectural covert channels can be addressed using a mixture of hardware and software mitigation techniques. These include partitioned caches, new barrier and flush instructions, and disabling high resolution performance counters and timers.
- [Requirements] Microarchitectural covert channels can be addressed using a mixture of hardware and software mitigation techniques. These include partitioned caches, new barrier and flush instructions, and disabling high resolution performance counters and timers.

## Demonstrative Examples (summary)
- On some processors the hardware indirect branch predictor is shared between execution contexts, for example, between sibling SMT threads. When SMT thread A executes an indirect branch to a target address X, this target may be temporarily stored by the indirect branch predictor. A subsequent indirect branch mis-prediction for SMT thread B could speculatively execute instructions at X (or at a location in B's address space that partially aliases X). Even though the processor rolls back the architectural effects of the mis-predicted indirect branch, the memory accesses alter data cache state, which is not rolled back after the indirect branch is resolved.
