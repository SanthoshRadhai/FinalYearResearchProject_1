# CWE-440: Expected Behavior Violation

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/440.html  

## Description
A feature, API, or function does not perform according to its specification.

## Related Weaknesses
- ChildOf: CWE-684

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Demonstrative Examples (summary)
- The provided code is extracted from the Control and Status Register (CSR), csr_regfile, module within the Hack@DAC'21 OpenPiton System-on-Chip (SoC). This module is designed to implement CSR registers in accordance with the RISC-V specification. The mie (machine interrupt enable) register is a 64-bit register [REF-1384], where bits correspond to different interrupt sources. As the name suggests, mie is a machine-level register that determines which interrupts are enabled. Note that in the example below the mie_q and mie_d registers represent the conceptual mie reigster in the RISC-V specification. The mie_d register is the value to be stored in the mie register while the mie_q register holds the current value of the mie register [REF-1385].
