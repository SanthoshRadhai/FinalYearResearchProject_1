# CWE-283: Unverified Ownership

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/283.html  

## Description
The product does not properly verify that a critical resource is owned by the proper entity.

## Related Weaknesses
- ChildOf: CWE-282

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — An attacker could gain unauthorized access to system resources.

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design] Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Demonstrative Examples (summary)
- This function is part of a privileged program that takes input from users with potentially lower privileges.
