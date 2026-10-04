# CWE-1221: Incorrect Register Defaults or Module Parameters

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1221.html  

## Description
Hardware description language code incorrectly defines register defaults or hardware Intellectual Property (IP) parameters to insecure values.

## Extended Description
Integrated circuits and hardware IP software programmable controls and settings are commonly stored in register circuits. These register contents have to be initialized at hardware reset to defined default values that are hard coded in the hardware description language (HDL) code of the hardware unit. Hardware descriptive languages also support definition of parameter variables, which can be defined in code during instantiation of the hardware IP module. Such parameters are generally used to configure a specific instance of a hardware IP in the design. The system security settings of a hardware design can be affected by incorrectly defined default values or IP parameters. The hardware IP would be in an insecure state at power reset, and this can be exposed or exploited by untrusted software running on the system. Both register defaults and parameters are hardcoded values, which cannot be changed using software or firmware patches but must be changed in hardware silicon. Thus, such security issues are considerably more difficult to address later in the lifecycle. Hardware designs can have a large number of such parameters and register defaults settings, and it is important to have design tool support to check these settings in an automated way and be able to identify which settings are security sensitive.

## Related Weaknesses
- ChildOf: CWE-1419

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Varies by Context — Degradation of system functionality, or loss of access control enforcement can occur.

## Potential Mitigations
- [Architecture and Design] During hardware design, all the system parameters and register defaults must be reviewed to identify security sensitive settings.
- [Implementation] The default values of these security sensitive settings need to be defined as part of the design review phase.

## Detection Methods
- [Automated Analysis] Use automated tools to test that values are configured per design specifications.

## Demonstrative Examples (summary)
- Consider example design module system verilog code shown below. The register_example module is an example parameterized module that defines two parameters, REGISTER_WIDTH and REGISTER_DEFAULT. Register_example module defines a Secure_mode setting, which when set makes the register content read-only and not modifiable by software writes. register_top module instantiates two registers, Insecure_Device_ID_1 and Insecure_Device_ID_2. Generally, registers containing device identifier values are required to be read only to prevent any possibility of software modifying these values.
- The example code is taken from the fuse memory inside the buggy OpenPiton SoC of HACK@DAC'21 [REF-1356]. Fuse memory can be used to store key hashes, password hashes, and configuration information. For example, the password hashes of JTAG and HMAC are stored in the fuse memory in the OpenPiton design.
- The following example code is excerpted from the Access Control module, acct_wrapper, in the Hack@DAC'21 buggy OpenPiton System-on-Chip (SoC). Within this module, a set of memory-mapped I/O registers, referred to as acct_mem, each 32-bit wide, is utilized to store access control permissions for peripherals [REF-1437]. Access control registers are typically used to define and enforce permissions and access rights for various system resources.
