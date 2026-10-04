# CWE-1274: Improper Access Control for Volatile Memory Containing Boot Code

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1274.html  

## Description
The product conducts a secure-boot process that transfers bootloader code from Non-Volatile Memory (NVM) into Volatile Memory (VM), but it does not have sufficient access control or other protections for the Volatile Memory.

## Extended Description
Adversaries could bypass the secure-boot process and execute their own untrusted, malicious boot code. As a part of a secure-boot process, the read-only-memory (ROM) code for a System-on-Chip (SoC) or other system fetches bootloader code from Non-Volatile Memory (NVM) and stores the code in Volatile Memory (VM), such as dynamic, random-access memory (DRAM) or static, random-access memory (SRAM). The NVM is usually external to the SoC, while the VM is internal to the SoC. As the code is transferred from NVM to VM, it is authenticated by the SoC's ROM code.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control, Integrity; Impact: Modify Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity — If the volatile-memory-region protections or access controls are insufficient to prevent modifications from an adversary or untrusted agent, the secure boot may be bypassed or replaced with the execution of an adversary's code.

## Potential Mitigations
- [Architecture and Design] Ensure that the design of volatile-memory protections is enough to prevent modification from an adversary or untrusted code.
- [Testing] Test the volatile-memory protections to ensure they are safe from modification or untrusted code.

## Detection Methods
- [Manual Analysis] Ensure the volatile memory is lockable or has locks. Ensure the volatile memory is locked for writes from untrusted agents or adversaries. Try modifying the volatile memory from an untrusted agent, and ensure these writes are dropped.
- [Manual Analysis] Analyze the device using the following steps: Identify all fabric master agents that are active during system Boot Flow when initial code is loaded from Non-volatile storage to volatile memory. Identify the volatile memory regions that are used for storing loaded system executable program. During system boot, test programming the identified memory regions in step 2 from all the masters identified in step 1. Only trusted masters should be allowed to write to the memory regions. For example, pluggable device peripherals should not have write access to program load memory regions.

## Demonstrative Examples (summary)
- A typical SoC secure boot's flow includes fetching the next piece of code (i.e., the boot loader) from NVM (e.g., serial, peripheral interface (SPI) flash), and transferring it to DRAM/SRAM volatile, internal memory, which is more efficient.
