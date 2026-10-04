# CWE-1317: Improper Access Control in Fabric Bridge

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1317.html  

## Description
The product uses a fabric bridge for transactions between two Intellectual Property (IP) blocks, but the bridge does not properly perform the expected privilege, identity, or other access control checks between those IP blocks.

## Extended Description
In hardware designs, different IP blocks are connected through interconnect-bus fabrics (e.g. AHB and OCP). Within a System on Chip (SoC), the IP block subsystems could be using different bus protocols. In such a case, the IP blocks are then linked to the central bus (and to other IP blocks) through a fabric bridge. Bridges are used as bus-interconnect-routing modules that link different protocols or separate, different segments of the overall SoC interconnect. For overall system security, it is important that the access-control privileges associated with any fabric transaction are consistently maintained and applied, even when they are routed or translated by a fabric bridge. A bridge that is connected to a fabric without security features forwards transactions to the slave without checking the privilege level of the master and results in a weakness in SoC access-control security. The same weakness occurs if a bridge does not check the hardware identity of the transaction received from the slave interface of the bridge.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control, Availability; Impact: DoS: Crash, Exit, or Restart, Bypass Protection Mechanism, Read Memory, Modify Memory

## Potential Mitigations
- [Architecture and Design] Ensure that the design includes provisions for access-control checks in the bridge for both upstream and downstream transactions.
- [Implementation] Implement access-control checks in the bridge for both upstream and downstream transactions.

## Detection Methods
- [Simulation / Emulation] RTL simulation to ensure that bridge-access controls are implemented properly.
- [Formal Verification] Formal verification of bridge RTL to ensure that access control cannot be bypassed.

## Demonstrative Examples (summary)
- This example is from CVE-2019-6260 [REF-1138]. The iLPC2AHB bridge connects a CPU (with multiple, privilege levels, such as user, super user, debug, etc.) over AHB interface to an LPC bus. Several peripherals are connected to the LPC bus. The bridge is expected to check the privilege level of the transactions initiated in the core before forwarding them to the peripherals on the LPC bus.
- The example code below is taken from the AES and core local interrupt (CLINT) peripherals of the HACK@DAC'21 buggy OpenPiton SoC. The access to all the peripherals for a given privilege level of the processor is controlled by an access control module in the SoC. This ensures that malicious users with insufficient privileges do not get access to sensitive data, such as the AES keys used by the operating system to encrypt and decrypt information. The security of the entire system will be compromised if the access controls are incorrectly enforced. The access controls are enforced through the interconnect-bus fabrics, where access requests with insufficient access control permissions will be rejected.
