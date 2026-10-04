# CWE-1419: Incorrect Initialization of Resource

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1419.html  

## Description
The product attempts to initialize a resource but does not correctly do so, which might leave the resource in an unexpected, incorrect, or insecure state when it is accessed.

## Extended Description
This can have security implications when the associated resource is expected to have certain properties or values. Examples include a variable that determines whether a user has been authenticated or not, or a register or fuse value that determines the security state of the product. For software, this weakness can frequently occur when implicit initialization is used, meaning the resource is not explicitly set to a specific value. For example, in C, memory is not necessarily cleared when it is allocated on the stack, and many scripting languages use a default empty, null value, or zero value when a variable is not explicitly initialized. For hardware, this weakness frequently appears with reset values and fuses. After a product reset, hardware may initialize registers incorrectly. During different phases of a product lifecycle, fuses may be set to incorrect values. Even if fuses are set to correct values, the lines to the fuse could be broken or there might be hardware on the fuse line that alters the fuse value to be incorrect.

## Related Weaknesses
- ChildOf: CWE-665

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data, Unexpected State
- Scope: Authorization, Integrity; Impact: Gain Privileges or Assume Identity
- Scope: Other; Impact: Varies by Context — The technical impact can vary widely based on how the resource is used in the product, and whether its contents affect security decisions.

## Potential Mitigations
- [Implementation] Choose the safest-possible initialization for security-related resources.
- [Implementation] Ensure that each resource (whether variable, memory buffer, register, etc.) is fully initialized.
- [Implementation] Pay close attention to complex conditionals or reset sources that affect initialization, since some paths might not perform the initialization.
- [Architecture and Design] Ensure that the design and architecture clearly identify what the initialization should be, and that the initialization does not have security implications.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Consider example design module system verilog code shown below. The register_example module is an example parameterized module that defines two parameters, REGISTER_WIDTH and REGISTER_DEFAULT. Register_example module defines a Secure_mode setting, which when set makes the register content read-only and not modifiable by software writes. register_top module instantiates two registers, Insecure_Device_ID_1 and Insecure_Device_ID_2. Generally, registers containing device identifier values are required to be read only to prevent any possibility of software modifying these values.
- This code attempts to login a user using credentials from a POST request:
- The following example code is excerpted from the Access Control module, acct_wrapper, in the Hack@DAC'21 buggy OpenPiton System-on-Chip (SoC). Within this module, a set of memory-mapped I/O registers, referred to as acct_mem, each 32-bit wide, is utilized to store access control permissions for peripherals [REF-1437]. Access control registers are typically used to define and enforce permissions and access rights for various system resources.
