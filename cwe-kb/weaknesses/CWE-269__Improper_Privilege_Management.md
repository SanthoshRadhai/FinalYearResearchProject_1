# CWE-269: Improper Privilege Management

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/269.html  

## Description
The product does not properly assign, modify, track, or check privileges for an actor, creating an unintended sphere of control for that actor.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design] Follow the principle of least privilege when assigning access rights to entities in a software system.
- [Architecture and Design] Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This code temporarily raises the program's privileges to allow creation of a new user folder.
- The following example demonstrates the weakness.
- The following example demonstrates the weakness.
- This code intends to allow only Administrators to print debug information about a system.
- This code allows someone with the role of "ADMIN" or "OPERATOR" to reset a user's password. The role of "OPERATOR" is intended to have less privileges than an "ADMIN", but still be able to help users with small issues such as forgotten passwords.
