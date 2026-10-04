# CWE-279: Incorrect Execution-Assigned Permissions

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/279.html  

## Description
While it is executing, the product sets the permissions of an object in a way that violates the intended permissions that have been specified by the user.

## Related Weaknesses
- ChildOf: CWE-732

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
