# CWE-1281: Sequence of Processor Instructions Leads to Unexpected Behavior

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1281.html  

## Description
Specific combinations of processor instructions lead to undesirable behavior such as locking the processor until a hard reset performed.

## Extended Description
If the instruction set architecture (ISA) and processor logic are not designed carefully and tested thoroughly, certain combinations of instructions may lead to locking the processor or other unexpected and undesirable behavior. Upon encountering unimplemented instruction opcodes or illegal instruction operands, the processor should throw an exception and carry on without negatively impacting security. However, specific combinations of legal and illegal instructions may cause unexpected behavior with security implications such as allowing unprivileged programs to completely lock the CPU.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Integrity, Availability; Impact: Varies by Context

## Potential Mitigations
- [Testing] Implement a rigorous testing strategy that incorporates randomization to explore instruction sequences that are unlikely to appear in normal workloads in order to identify halt and catch fire instruction sequences.
- [Patching and Maintenance] Patch operating system to avoid running Halt and Catch Fire type sequences or to mitigate the damage caused by unexpected behavior. See [REF-1108].

## Demonstrative Examples (summary)
- The Pentium F00F bug is a real-world example of how a sequence of instructions can lock a processor. The "cmpxchg8b" instruction compares contents of registers with a memory location. The operand is expected to be a memory location, but in the bad code snippet it is the eax register. Because the specified operand is illegal, an exception is generated, which is the correct behavior and not a security issue in itself. However, when prefixed with the "lock" instruction, the processor deadlocks because locked memory transactions require a read and write pair of transactions to occur before the lock on the memory bus is released. The exception causes a read to occur but there is no corresponding write, as there would have been if a legal operand had been supplied to the cmpxchg8b instruction. [REF-1331]
- The Cyrix Coma bug was capable of trapping a Cyrix 6x86, 6x86L, or 6x86MX processor in an infinite loop. An infinite loop on a processor is not necessarily an issue on its own, as interrupts could stop the loop. However, on select Cyrix processors, the x86 Assembly 'xchg' instruction was designed to prevent interrupts. On these processors, if the loop was such that a new 'xchg' instruction entered the instruction pipeline before the previous one exited, the processor would become deadlocked. [REF-1323]
- The Motorola MC6800 microprocessor contained the first documented instance of a Halt and Catch Fire instruction - an instruction that causes the normal function of a processor to stop. If the MC6800 was given the opcode 0x9D or 0xDD, the processor would begin to read all memory very quickly, in sequence, and without executing any other instructions. This will cause the processor to become unresponsive to anything but a hard reset. [REF-1324]
- The example code is taken from the commit stage inside the processor core of the HACK@DAC'19 buggy CVA6 SoC [REF-1342]. To ensure the correct execution of atomic instructions, the CPU must guarantee atomicity: no other device overwrites the memory location between the atomic read starts and the atomic write finishes. Another device may overwrite the memory location only before the read operation or after the write operation, but never between them, and finally, the content will still be consistent.
