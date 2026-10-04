# CWE-1253: Incorrect Selection of Fuse Values

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1253.html  

## Description
The logic level used to set a system to a secure state relies on a fuse being unblown.

## Extended Description
Fuses are often used to store secret data, including security configuration data. When not blown, a fuse is considered to store a logic 0, and, when blown, it indicates a logic 1. Fuses are generally considered to be one-directional, i.e., once blown to logic 1, it cannot be reset to logic 0.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — If the logic used to determine system-security state (by leveraging the values sensed from the fuses) uses negative logic, an attacker might blow the fuse and drive the system to an insecure state.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart
- Scope: Confidentiality; Impact: Read Memory
- Scope: Integrity; Impact: Modify Memory, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design] Logic should be designed in a way that blown fuses do not put the product into an insecure state that can be leveraged by an attacker.

## Demonstrative Examples (summary)
- A chip implements a secure boot and uses the sensed value of a fuse "do_secure_boot" to determine whether to perform a secure boot or not. If this fuse value is "0", the system performs secure boot. Otherwise, it does not perform secure boot. An attacker blows the "do_secure_boot" fuse to "1". After reset, the attacker loads a custom bootloader, and, since the fuse value is now "1", the system does not perform secure boot, and the attacker can execute their custom firmware image. Since by default, a fuse-configuration value is a "0", an attacker can blow it to a "1" with inexpensive hardware. If the logic is reversed, an attacker cannot easily reset the fuse. Note that, with specialized and expensive equipment, an attacker with full physical access might be able to "unblow" the fuse value to a "0".
