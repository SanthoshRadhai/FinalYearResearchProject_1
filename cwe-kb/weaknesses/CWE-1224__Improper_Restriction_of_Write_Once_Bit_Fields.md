# CWE-1224: Improper Restriction of Write-Once Bit Fields

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1224.html  

## Description
The hardware design control register "sticky bits" or write-once bit fields are improperly implemented, such that they can be reprogrammed by software.

## Extended Description
Integrated circuits and hardware IP software programmable controls and settings are commonly stored in register circuits. These register contents have to be initialized at hardware reset to define default values that are hard coded in the hardware description language (HDL) code of the hardware unit. A common security protection method used to protect register settings from modification by software is to make the settings write-once or "sticky." This allows writing to such registers only once, whereupon they become read-only. This is useful to allow initial boot software to configure systems settings to secure values while blocking runtime software from modifying such hardware settings. Failure to implement write-once restrictions in hardware design can expose such registers to being re-programmed by software and written multiple times. For example, write-once fields could be implemented to only be write-protected if they have been set to value "1", wherein they would work as "write-1-once" and not "write-once".

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Varies by Context — System configuration cannot be programmed in a secure way.

## Potential Mitigations
- [Architecture and Design] During hardware design, all register write-once or sticky fields must be evaluated for proper configuration.

## Detection Methods
- [Automated Analysis] Use automated tools to test that values are not reprogrammable and that write-once fields lock on writing zeros.

## Demonstrative Examples (summary)
- Consider the example design module system verilog code shown below. register_write_once_example module is an example of register that has a write-once field defined. Bit 0 field captures the write_once_status value. This implementation can be for a register that is defined by specification to be a write-once register, since the write_once_status field gets written by input data bit 0 on first write.
