# CWE-1256: Improper Restriction of Software Interfaces to Hardware Features

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1256.html  

## Description
The product provides software-controllable device functionality for capabilities such as power and clock management, but it does not properly limit functionality that can lead to modification of hardware memory or register bits, or the ability to observe physical side channels.

## Extended Description
It is frequently assumed that physical attacks such as fault injection and side-channel analysis require an attacker to have physical access to the target device. This assumption may be false if the device has improperly secured power management features, or similar features. For mobile devices, minimizing power consumption is critical, but these devices run a wide variety of applications with different performance requirements. Software-controllable mechanisms to dynamically scale device voltage and frequency and monitor power consumption are common features in today's chipsets, but they also enable attackers to mount fault injection and side-channel attacks without having physical access to the device. Fault injection attacks involve strategic manipulation of bits in a device to achieve a desired effect such as skipping an authentication step, elevating privileges, or altering the output of a cryptographic operation. Manipulation of the device clock and voltage supply is a well-known technique to inject faults and is cheap to implement with physical device access. Poorly protected power management features allow these attacks to be performed from software. Other features, such as the ability to write repeatedly to DRAM at a rapid rate from unprivileged software, can result in bit flips in other memory locations (Rowhammer, [REF-1083]). Side channel analysis requires gathering measurement traces of physical quantities such as power consumption. Modern processors often include power metering capabilities in the hardware itself (e.g., Intel RAPL) which if not adequately protected enable attackers to gather measurements necessary for performing side-channel attacks from software.

## Related Weaknesses
- ChildOf: CWE-285

## Common Consequences
- Scope: Integrity; Impact: Modify Memory, Modify Application Data, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design, Implementation] Ensure proper access control mechanisms protect software-controllable features altering physical operating conditions such as clock frequency and voltage.

## Detection Methods
- [Manual Analysis] Perform a security evaluation of system-level architecture and design with software-aided physical attacks in scope.
- [Automated Dynamic Analysis] Use custom software to change registers that control clock settings or power settings to try to bypass security locks, or repeatedly write DRAM to try to change adjacent locations. This can be effective in extracting or changing data. The drawback is that it cannot be run before manufacturing, and it may require specialized software.

## Demonstrative Examples (summary)
- This example considers the Rowhammer problem [REF-1083]. The Rowhammer issue was caused by a program in a tight loop writing repeatedly to a location to which the program was allowed to write but causing an adjacent memory location value to change.
- Suppose a hardware design implements a set of software-accessible registers for scaling clock frequency and voltage but does not control access to these registers. Attackers may cause register and memory changes and race conditions by changing the clock or voltage of the device under their control.
- Consider the following SoC design. Security-critical settings for scaling clock frequency and voltage are available in a range of registers bounded by [PRIV_END_ADDR : PRIV_START_ADDR] in the tmcu.csr module in the HW Root of Trust. These values are writable based on the lock_bit register in the same module. The lock_bit is only writable by privileged software running on the tmcu.
