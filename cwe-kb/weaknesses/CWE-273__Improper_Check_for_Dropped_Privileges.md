# CWE-273: Improper Check for Dropped Privileges

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/273.html  

## Description
The product attempts to drop privileges but does not check or incorrectly checks to see if the drop succeeded.

## Extended Description
If the drop fails, the product will continue to run with the raised privileges, which might provide additional access to unprivileged users.

## Related Weaknesses
- ChildOf: CWE-754
- ChildOf: CWE-754
- ChildOf: CWE-271
- PeerOf: CWE-252

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — If privileges are not dropped, neither are access rights of the user. Often these rights can be prevented from being dropped.
- Scope: Access Control, Non-Repudiation; Impact: Gain Privileges or Assume Identity, Hide Activities — If privileges are not dropped, in some cases the system may record actions as the user which is being impersonated rather than the impersonator.

## Potential Mitigations
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- [Implementation] Check the results of all functions that return a value and verify that the value is expected.
- [Implementation] In Windows, make sure that the process token has the SeImpersonatePrivilege(Microsoft Server 2003). Code that relies on impersonation for security must ensure that the impersonation succeeded, i.e., that a proper privilege demotion happened.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code attempts to take on the privileges of a user before creating a file, thus avoiding performing the action with unnecessarily high privileges:
