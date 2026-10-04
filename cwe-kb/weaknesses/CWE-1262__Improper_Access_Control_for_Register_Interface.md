# CWE-1262: Improper Access Control for Register Interface

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1262.html  

## Description
The product uses memory-mapped I/O registers that act as an interface to hardware functionality from software, but there is improper access control to those registers.

## Extended Description
Software commonly accesses peripherals in a System-on-Chip (SoC) or other device through a memory-mapped register interface. Malicious software could tamper with any security-critical hardware data that is accessible directly or indirectly through the register interface, which could lead to a loss of confidentiality and integrity.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Memory, Read Application Data, Modify Memory, Modify Application Data, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Unexpected State, Alter Execution Logic — Confidentiality of hardware assets may be violated if the protected information can be read out by software through the register interface. Registers storing security state, settings, other security-critical data may be corruptible by software without correctly implemented protections.

## Potential Mitigations
- [Architecture and Design] Design proper policies for hardware register access from software.
- [Implementation] Ensure that access control policies for register access are implemented in accordance with the specified design.

## Detection Methods
- [Manual Analysis] This is applicable in the Architecture phase before implementation started. Make sure access policy is specified for the entire memory map. Manual analysis may not ensure the implementation is correct.
- [Manual Analysis] Registers controlling hardware should have access control implemented. This access control may be checked manually for correct implementation. Items to check consist of how are trusted parties set, how are trusted parties verified, how are accesses verified, etc. Effectiveness of a manual analysis will vary depending upon how complicated the interface is constructed.
- [Simulation / Emulation] Functional simulation is applicable during the Implementation Phase. Testcases must be created and executed for memory mapped registers to verify adherence to the access control policy. This method can be effective, since functional verification needs to be performed on the design, and verification for this weakness will be included. There can be difficulty covering the entire memory space during the test.
- [Formal Verification] Formal verification is applicable during the Implementation phase. Assertions need to be created in order to capture illegal register access scenarios and prove that they cannot occur. Formal methods are exhaustive and can be very effective, but creating the cases for large designs may be complex and difficult.
- [Automated Analysis] Information flow tracking can be applicable during the Implementation phase. Security sensitive data (assets) - for example, as stored in registers - is automatically tracked over time through the design to verify the data doesn't reach illegal destinations that violate the access policies for the memory map. This method can be very effective when used together with simulation and emulation, since detecting violations doesn't rely on specific scenarios or data values. This method does rely on simulation and emulation, so testcases must exist in order to use this method.
- [Architecture or Design Review] Manual documentation review of the system memory map, register specification, and permissions associated with accessing security-relevant functionality exposed via memory-mapped registers.
- [Fuzzing] Perform penetration testing (either manual or semi-automated with fuzzing) to verify that access control mechanisms such as the memory protection units or on-chip bus firewall settings adequately protect critical hardware registers from software access.

## Demonstrative Examples (summary)
- The register interface provides software access to hardware functionality. This functionality is an attack surface. This attack surface may be used to run untrusted code on the system through the register interface. As an example, cryptographic accelerators require a mechanism for software to select modes of operation and to provide plaintext or ciphertext data to be encrypted or decrypted as well as other functions. This functionality is commonly provided through registers.
- The example code is taken from the Control/Status Register (CSR) module inside the processor core of the HACK@DAC'19 buggy CVA6 SoC [REF-1340]. In RISC-V ISA [REF-1341], the CSR file contains different sets of registers with different privilege levels, e.g., user mode (U), supervisor mode (S), hypervisor mode (H), machine mode (M), and debug mode (D), with different read-write policies, read-only (RO) and read-write (RW). For example, machine mode, which is the highest privilege mode in a RISC-V system, registers should not be accessible in user, supervisor, or hypervisor modes.
