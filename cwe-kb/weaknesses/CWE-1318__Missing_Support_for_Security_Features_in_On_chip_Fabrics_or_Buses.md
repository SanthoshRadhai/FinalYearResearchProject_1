# CWE-1318: Missing Support for Security Features in On-chip Fabrics or Buses

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1318.html  

## Description
On-chip fabrics or buses either do not support or are not configured to support privilege separation or other security features, such as access control.

## Extended Description
Certain on-chip fabrics and buses, especially simple and low-power buses, do not support security features. Apart from data transfer and addressing ports, some fabrics and buses do not have any interfaces to transfer privilege, immutable identity, or any other security attribute coming from the bus master. Similarly, they do not have dedicated signals to transport security-sensitive data from slave to master, such as completions for certain types of transactions. Few other on-chip fabrics and buses support security features and define specific interfaces/signals for transporting security attributes from master to slave or vice-versa. However, including these signals is not mandatory and could be left unconfigured when generating the register-transfer-level (RTL) description for the fabric. Such fabrics or buses should not be used to transport any security attribute coming from the bus master. In general, peripherals with security assets should not be connected to such buses before the transaction from the bus master reaches the bus, unless some form of access control is performed at a fabric bridge or another intermediate module.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control, Availability; Impact: DoS: Crash, Exit, or Restart, Read Memory, Modify Memory

## Potential Mitigations
- [Architecture and Design] If fabric does not support security features, implement security checks in a bridge or any component that is between the master and the fabric. Alternatively, connect all fabric slaves that do not have any security assets under one such fabric and connect peripherals with security assets to a different fabric that supports security features.

## Detection Methods
- [Architecture or Design Review] Review the fabric specification and ensure that it contains signals to transfer security-sensitive signals.
- [Manual Static Analysis - Source Code] Lack of security features can also be confirmed through manual RTL review of the fabric RTL.

## Demonstrative Examples (summary)
- Several systems on chips (SoCs) use the Advanced-Microcontroller Bus Architecture (AMBA) Advanced-Peripheral Bus (APB) protocol. APB is a simple, low-power bus and uses the PPROT[2:0] bits to indicate the security state of the bus masters ;PPROT[0] indicates privilege, PPROT[1] indicates secure/non-secure transaction, and PPROT[2] indicates instruction/data. Assume that there is no fabric bridge in the SoC. One of the slaves, the power-management unit, contains registers that store the thermal-shutdown limits.
- The Open-Core-Protocol (OCP) fabric supports two configurable, width-optional signals for transporting security attributes: MReqInfo and SRespInfo. MReqInfo is used to transport security attributes from bus master to slave, and SRespInfo is used to transport security attributes from slave to bus master. An SoC uses OCP to connect several bus masters, each with a unique and immutable hardware identity, to several slaves. One of the bus masters, the CPU, reports the privilege level (user or super user) in addition to the unique identity. One of the slaves, the power-management unit, contains registers that store the thermal-shutdown limits.
