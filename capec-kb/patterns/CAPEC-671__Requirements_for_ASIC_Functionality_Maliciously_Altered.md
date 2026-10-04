# CAPEC-671: Requirements for ASIC Functionality Maliciously Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/671.html  

## Description
An adversary with access to functional requirements for an application specific integrated circuit (ASIC), a chip designed/customized for a singular particular use, maliciously alters requirements derived from originating capability needs. In the chip manufacturing process, requirements drive the chip design which, when the chip is fully manufactured, could result in an ASIC which may not meet the user’s needs, contain malicious functionality, or exhibit other anomalous behaviors thereby affecting the intended use of the ASIC.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- An adversary would need to have access to a foundry’s or chip maker’s requirements management system that stores customer requirements for ASICs, requirements upon which the design of the ASIC is based.

## Skills Required
- [High] An adversary would need experience in designing chips based on functional requirements in order to manipulate requirements in such a way that deviations would not be detected in subsequent stages of ASIC manufacture and where intended malicious functionality would be available to the adversary once integrated into a system and fielded.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for hardware requirements and design.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.
