# CWE-455: Non-exit on Failed Initialization

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/455.html  

## Description
The product does not exit or otherwise modify its operation when security-relevant errors occur during initialization, such as when a configuration file has a format error or a hardware security module (HSM) cannot be activated, which can cause the product to execute in a less secure fashion than intended by the administrator.

## Related Weaknesses
- ChildOf: CWE-665
- ChildOf: CWE-705
- ChildOf: CWE-636

## Common Consequences
- Scope: Integrity, Other; Impact: Modify Application Data, Alter Execution Logic — The application could be placed in an insecure state that may allow an attacker to modify sensitive data or allow unintended logic to be executed.

## Potential Mitigations
- [Implementation] Follow the principle of failing securely when an error occurs. The system should enter a state where it is not vulnerable and will not display sensitive error messages to a potential attacker.

## Demonstrative Examples (summary)
- The following code intends to limit certain operations to the administrator only.
