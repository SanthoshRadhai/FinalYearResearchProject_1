# CWE-1315: Improper Setting of Bus Controlling Capability in Fabric End-point

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1315.html  

## Description
The bus controller enables bits in the fabric end-point to allow responder devices to control transactions on the fabric.

## Extended Description
To support reusability, certain fabric interfaces and end points provide a configurable register bit that allows IP blocks connected to the controller to access other peripherals connected to the fabric. This allows the end point to be used with devices that function as a controller or responder. If this bit is set by default in hardware, or if firmware incorrectly sets it later, a device intended to be a responder on a fabric is now capable of controlling transactions to other devices and might compromise system security.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control; Impact: Modify Memory, Read Memory, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.
- [Implementation] For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.
- [System Configuration] For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.

## Demonstrative Examples (summary)
- A typical, phone platform consists of the main, compute core or CPU, a DRAM-memory chip, an audio codec, a baseband modem, a power-management-integrated circuit ("PMIC"), a connectivity (WiFi and Bluetooth) modem, and several other analog/RF components. The main CPU is the only component that can control transactions, and all the other components are responder-only devices. All the components implement a PCIe end-point to interface with the rest of the platform. The responder devices should have the bus-control-enable bit in the PCIe-end-point register set to 0 in hardware to prevent the devices from controlling transactions to the CPU or other peripherals.
