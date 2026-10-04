# CAPEC-674: Design for FPGA Maliciously Altered

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/674.html  

## Description
An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the FPGA performing or enabling malicious functions on a host system. Prior to the memory chip reload, the adversary alters the program for the FPGA by adding a function to impact system operation.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- An adversary would need to have access to FPGA programming/configuration-related systems in a chip maker’s development environment where FPGAs can be initially configured prior to delivery to a customer or have access to such systems in a customer facility where end-user FPGA configuration/reconfiguration can be performed.

## Skills Required
- [High] An adversary would need to be skilled in FPGA programming in order to create/manipulate configurations in such a way that when loaded into an FPGA, the end user would be able to observe through testing all user-defined required functions but would be unaware of any additional functions the adversary may have introduced.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for FPGA programming and program uploads to FPGA chips.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.
