# CWE-1330: Remanent Data Readable after Memory Erase

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1330.html  

## Description
Confidential information stored in memory circuits is readable or recoverable after being cleared or erased.

## Extended Description
Data remanence occurs when stored, memory content is not fully lost after a memory-clear or -erase operation. Confidential memory contents can still be readable through data remanence in the hardware. Data remanence can occur because of performance optimization or memory organization during 'clear' or 'erase' operations, like a design that allows the memory-organization metadata (e.g., file pointers) to be erased without erasing the actual memory content. To protect against this weakness, memory devices will often support different commands for optimized memory erase and explicit secure erase. Data remanence can also happen because of the physical properties of memory circuits in use. For example, static, random-access-memory (SRAM) and dynamic, random-access-memory (DRAM) data retention is based on the charge retained in the memory cell, which depends on factors such as power supply, refresh rates, and temperature. Other than explicit erase commands, self-encrypting, secure-memory devices can also support secure erase through cryptographic erase commands. In such designs, only the decryption keys for encrypted data stored on the device are erased. That is, the stored data are always remnant in the media after a cryptographic erase. However, only the encrypted data can be extracted. Thus, protection against data recovery in such designs relies on the strength of the encryption algorithm.

## Related Weaknesses
- ChildOf: CWE-1301
- ChildOf: CWE-1301

## Common Consequences
- Scope: Confidentiality; Impact: Modify Memory, Read Memory — Confidential data are readable to untrusted agent.

## Potential Mitigations
- [Architecture and Design] Support for secure-erase commands that apply multiple cycles of overwriting memory with known patterns and of erasing actual content. Support for cryptographic erase in self-encrypting, memory devices. External, physical tools to erase memory such as ultraviolet-rays-based erase of Electrically erasable, programmable, read-only memory (EEPROM). Physical destruction of media device. This is done for repurposed or scrapped devices that are no longer in use.

## Detection Methods
- [Architecture or Design Review] Testing of memory-device contents after clearing or erase commands. Dynamic analysis of memory contents during device operation to detect specific, confidential assets. Architecture and design analysis of memory clear and erase operations.
- [Dynamic Analysis with Manual Results Interpretation] Testing of memory-device contents after clearing or erase commands. Dynamic analysis of memory contents during device operation to detect specific, confidential assets. Architecture and design analysis of memory clear and erase operations.

## Demonstrative Examples (summary)
- Consider a device that uses flash memory for non-volatile-data storage. To optimize flash-access performance or reliable-flash lifetime, the device might limit the number of flash writes/erases by maintaining some state in internal SRAM and only committing changes to flash memory periodically.
