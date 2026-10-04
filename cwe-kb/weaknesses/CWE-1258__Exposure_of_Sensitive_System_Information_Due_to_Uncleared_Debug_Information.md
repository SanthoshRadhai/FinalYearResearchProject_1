# CWE-1258: Exposure of Sensitive System Information Due to Uncleared Debug Information

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1258.html  

## Description
The hardware does not fully clear security-sensitive values, such as keys and intermediate values in cryptographic operations, when debug mode is entered.

## Extended Description
Security sensitive values, keys, intermediate steps of cryptographic operations, etc. are stored in temporary registers in the hardware. If these values are not cleared when debug mode is entered they may be accessed by a debugger allowing sensitive information to be accessible by untrusted parties.

## Related Weaknesses
- ChildOf: CWE-212

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Whenever debug mode is enabled, all registers containing sensitive assets must be cleared.

## Demonstrative Examples (summary)
- A cryptographic core in a System-On-a-Chip (SoC) is used for cryptographic acceleration and implements several cryptographic operations (e.g., computation of AES encryption and decryption, SHA-256, HMAC, etc.). The keys for these operations or the intermediate values are stored in registers internal to the cryptographic core. These internal registers are in the Memory Mapped Input Output (MMIO) space and are blocked from access by software and other untrusted agents on the SoC. These registers are accessible through the debug and test interface.
- The following code example is extracted from the AES wrapper module, aes1_wrapper, of the Hack@DAC'21 buggy OpenPiton System-on-Chip (SoC). Within this wrapper module are four memory-mapped registers: core_key, core_key0, core_key1, and core_key2. Core_key0, core_key1, and core_key2 hold encryption/decryption keys. The core_key register selects a key and sends it to the underlying AES module to execute encryption/decryption operations. Debug mode in processors and SoCs facilitates design debugging by granting access to internal signal/register values, including physical pin values of peripherals/core, fabric bus data transactions, and inter-peripheral registers. Debug mode allows users to gather detailed, low-level information about the design to diagnose potential issues. While debug mode is beneficial for diagnosing processors or SoCs, it also introduces a new attack surface for potential attackers. For instance, if an attacker gains access to debug mode, they could potentially read any content transmitted through the fabric bus or access encryption/decryption keys stored in cryptographic peripherals. Therefore, it is crucial to clear the contents of secret registers upon entering debug mode. In the provided example of flawed code below, when debug_mode_i is activated, the register core_key0 is set to zero to prevent AES key leakage during debugging. However, this protective measure is not applied to the core_key1 register [REF-1435], leaving its contents uncleared during debug mode. This oversight enables a debugger to access sensitive information. Failing to clear sensitive data during debug mode may lead to unauthorized access to secret keys and compromise system security.
