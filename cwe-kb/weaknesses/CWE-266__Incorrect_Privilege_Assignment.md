# CWE-266: Incorrect Privilege Assignment

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/266.html  

## Description
A product incorrectly assigns a privilege to a particular actor, creating an unintended sphere of control for that actor.

## Related Weaknesses
- ChildOf: CWE-269
- CanAlsoBe: CWE-286

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — A user can access restricted functionality and/or sensitive information that may include administrative functionality and user accounts.

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design, Operation] Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
- The following example demonstrates the weakness.
- This application sends a special intent with a flag that allows the receiving application to read a data file for backup purposes.
