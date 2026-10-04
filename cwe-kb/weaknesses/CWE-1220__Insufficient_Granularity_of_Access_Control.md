# CWE-1220: Insufficient Granularity of Access Control

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1220.html  

## Description
The product implements access controls via a policy or other feature with the intention to disable or restrict accesses (reads and/or writes) to assets in a system from untrusted agents. However, implemented access controls lack required granularity, which renders the control policy too broad because it allows accesses from unauthorized agents to the security-sensitive assets.

## Extended Description
Integrated circuits and hardware engines can expose accesses to assets (device configuration, keys, etc.) to trusted firmware or a software module (commonly set by BIOS/bootloader). This access is typically access-controlled. Upon a power reset, the hardware or system usually starts with default values in registers, and the trusted firmware (Boot firmware) configures the necessary access-control protection. A common weakness that can exist in such protection schemes is that access controls or policies are not granular enough. This condition allows agents beyond trusted agents to access assets and could lead to a loss of functionality or the ability to set up the device securely. This further results in security risks from leaked, sensitive, key material to modification of device configuration.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Other

## Potential Mitigations
- [Architecture and Design, Implementation, Testing] Access-control-policy protections must be reviewed for design inconsistency and common weaknesses. Access-control-policy definition and programming flow must be tested in pre-silicon, post-silicon testing.

## Demonstrative Examples (summary)
- Consider a system with a register for storing AES key for encryption or decryption. The key is 128 bits, implemented as a set of four 32-bit registers. The key registers are assets and registers, AES_KEY_READ_POLICY and AES_KEY_WRITE_POLICY, and are defined to provide necessary access controls. The read-policy register defines which agents can read the AES-key registers, and write-policy register defines which agents can program or write to those registers. Each register is a 32-bit register, and it can support access control for a maximum of 32 agents. The number of the bit when set (i.e., "1") allows respective action from an agent whose identity matches the number of the bit and, if "0" (i.e., Clear), disallows the respective action to that corresponding agent.
- Within the AXI node interface wrapper module in the RISC-V AXI module of the HACK@DAC'19 CVA6 SoC [REF-1346], an access control mechanism is employed to regulate the access of different privileged users to peripherals.
- Consider the following SoC design. The sram in HRoT has an address range that is readable and writable by unprivileged software and it has an area that is only readable by unprivileged software. The tbus interconnect enforces access control for subordinates on the bus but uses only one bit to control both read and write access. Address 0xA0000000 - 0xA000FFFF is readable and writable by the untrusted cores core{0-N} and address 0xA0010000 - 0xA001FFFF is only readable by the untrusted cores core{0-N}.
