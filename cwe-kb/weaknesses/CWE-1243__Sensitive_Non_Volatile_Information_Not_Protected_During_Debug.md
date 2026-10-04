# CWE-1243: Sensitive Non-Volatile Information Not Protected During Debug

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1243.html  

## Description
Access to security-sensitive information stored in fuses is not limited during debug.

## Extended Description
Several security-sensitive values are programmed into fuses to be used during early-boot flows or later at runtime. Examples of these security-sensitive values include root keys, encryption keys, manufacturing-specific information, chip-manufacturer-specific information, and original-equipment-manufacturer (OEM) data. After the chip is powered on, these values are sensed from fuses and stored in temporary locations such as registers and local memories. These locations are typically access-control protected from untrusted agents capable of accessing them. Even to trusted agents, only read-access is provided.

## Related Weaknesses
- ChildOf: CWE-1263

## Common Consequences
- Scope: Confidentiality, Access Control; Impact: Modify Memory, Read Memory, Bypass Protection Mechanism — If these locations are not blocked during debug operations, it can allow a user to access this sensitive information.

## Potential Mitigations
- [Architecture and Design, Implementation] Disable access to security-sensitive information stored in fuses directly and also reflected from temporary storage locations when in debug mode.

## Demonstrative Examples (summary)
- Sensitive manufacturing data (such as die information) are stored in fuses. When the chip powers on, these values are read from the fuses and stored in microarchitectural registers. These registers are only given read access to trusted software running on the core. Untrusted software running on the core is not allowed to access these registers.
- The example code below is taken from one of the AES cryptographic accelerators of the HACK@DAC'21 buggy OpenPiton SoC [REF-1366]. The operating system (OS) uses three AES keys to encrypt and decrypt sensitive data using this accelerator. These keys are sensitive data stored in fuses. The security of the OS will be compromised if any of these AES keys are leaked. During system bootup, these AES keys are sensed from fuses and stored in temporary hardware registers of the AES peripheral. Access to these temporary registers is disconnected during the debug state to prevent them from leaking through debug access. In this example (see the vulnerable code source), the registers key0, key1, and key2 are used to store the three AES keys (which are accessed through key_big0, key_big1, and key_big2 signals). The OS selects one of these three keys through the key_big signal, which is used by the AES engine.
