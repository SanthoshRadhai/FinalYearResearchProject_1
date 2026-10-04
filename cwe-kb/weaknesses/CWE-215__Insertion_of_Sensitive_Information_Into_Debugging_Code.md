# CWE-215: Insertion of Sensitive Information Into Debugging Code

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/215.html  

## Description
The product inserts sensitive information into debugging code, which could expose this information if the debugging code is not disabled in production.

## Extended Description
When debugging, it may be necessary to report detailed information to the programmer. However, if the debugging code is not disabled when the product is operating in a production environment, then this sensitive information may be exposed to attackers.

## Related Weaknesses
- ChildOf: CWE-200

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Implementation] Do not leave debug statements that could be executed in the source code. Ensure that all debug information is eradicated before releasing the software.
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following program changes its behavior based on a debug flag.
