# CWE-1422: Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1422.html  

## Description
A processor event or prediction may allow incorrect or stale data to be forwarded to transient operations, potentially exposing data over a covert channel.

## Extended Description
Software may use a variety of techniques to preserve the confidentiality of private data that is accessible within the current processor context. For example, the memory safety and type safety properties of some high-level programming languages help to prevent software written in those languages from exposing private data. As a second example, software sandboxes may co-locate multiple users' software within a single process. The processor's Instruction Set Architecture (ISA) may permit one user's software to access another user's data (because the software shares the same address space), but the sandbox prevents these accesses by using software techniques such as bounds checking. If incorrect or stale data can be forwarded (for example, from a cache) to transient operations, then the operations' microarchitectural side effects may correspond to the data. If an attacker can trigger these transient operations and observe their side effects through a covert channel, then the attacker may be able to infer the data. For example, an attacker process may induce transient execution in a victim process that causes the victim to inadvertently access and then expose its private data via a covert channel. In the software sandbox example, an attacker sandbox may induce transient execution in its own code, allowing it to transiently access and expose data in a victim sandbox that shares the same address space. Consequently, weaknesses that arise from incorrect/stale data forwarding might violate users' expectations of software-based memory safety and isolation techniques. If the data forwarding behavior is not properly documented by the hardware vendor, this might violate the software vendor's expectation of how the hardware should behave.

## Related Weaknesses
- ChildOf: CWE-1420
- ChildOf: CWE-1420

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory

## Potential Mitigations
- [Architecture and Design] The hardware designer can attempt to prevent transient execution from causing observable discrepancies in specific covert channels.
- [Requirements] Processor designers, system software vendors, or other agents may choose to restrict the ability of unprivileged software to access to high-resolution timers that are commonly used to monitor covert channels.
- [Requirements] Processor designers may expose instructions or other architectural features that allow software to mitigate the effects of transient execution, but without disabling predictors. These features may also help to limit opportunities for data exposure.
- [Requirements] Processor designers may expose registers (for example, control registers or model-specific registers) that allow privileged and/or user software to disable specific predictors or other hardware features that can cause confidential data to be exposed during transient execution.
- [Build and Compilation] Use software techniques (including the use of serialization instructions) that are intended to reduce the number of instructions that can be executed transiently after a processor event or misprediction.
- [Build and Compilation] Isolate sandboxes or managed runtimes in separate address spaces (separate processes).
- [Build and Compilation] Include serialization instructions (for example, LFENCE) that prevent processor events or mis-predictions prior to the serialization instruction from causing transient execution after the serialization instruction. For some weaknesses, a serialization instruction can also prevent a processor event or a mis-prediction from occurring after the serialization instruction (for example, CVE-2018-3639 can allow a processor to predict that a load will not depend on an older store; a serialization instruction between the store and the load may allow the store to update memory and prevent the mis-prediction from happening at all).
- [Build and Compilation] Use software techniques that can mitigate the consequences of transient execution. For example, address masking can be used in some circumstances to prevent out-of-bounds transient reads.
- [Build and Compilation] If the weakness is exposed by a single instruction (or a small set of instructions), then the compiler (or JIT, etc.) can be configured to prevent the affected instruction(s) from being generated, and instead generate an alternate sequence of instructions that is not affected by the weakness.
- [Documentation] If a hardware feature can allow incorrect or stale data to be forwarded to transient operations, the hardware designer may opt to disclose this behavior in architecture documentation. This documentation can inform users about potential consequences and effective mitigations.

## Detection Methods
- [Automated Static Analysis] A variety of automated static analysis tools can identify potentially exploitable code sequences in software. These tools may perform the analysis on source code, on binary code, or on an intermediate code representation (for example, during compilation).
- [Manual Analysis] This weakness can be detected in hardware by manually inspecting processor specifications. Features that exhibit this weakness may include microarchitectural predictors, access control checks that occur out-of-order, or any other features that can allow operations to execute without committing to architectural state.Hardware designers can also scrutinize aspects of the instruction set architecture that have undefined behavior; these can become a focal point when applying other detection methods.
- [Automated Analysis] Software vendors can release tools that detect presence of known weaknesses on a processor. For example, some of these tools can attempt to transiently execute a vulnerable code sequence and detect whether code successfully leaks data in a manner consistent with the weakness under test. Alternatively, some hardware vendors provide enumeration for the presence of a weakness (or lack of a weakness). These enumeration bits can be checked and reported by system software. For example, Linux supports these checks for many commodity processors: $ cat /proc/cpuinfo | grep bugs | head -n 1 bugs : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs taa itlb_multihit srbds mmio_stale_data retbleed

## Demonstrative Examples (summary)
- Faulting loads in a victim domain may trigger incorrect transient forwarding, which leaves secret-dependent traces in the microarchitectural state. Consider this code sequence example from [REF-1391].
- Some processors try to predict when a store will forward data to a subsequent load, even when the address of the store or the load is not yet known. For example, on Intel processors this feature is called a Fast Store Forwarding Predictor [REF-1392], and on AMD processors the feature is called Predictive Store Forwarding [REF-1393]. A misprediction can cause incorrect or stale data to be forwarded from a store to a load, as illustrated in the following code snippet from [REF-1393]:
