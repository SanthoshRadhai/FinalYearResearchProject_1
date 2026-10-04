# CWE-268: Privilege Chaining

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/268.html  

## Description
Two distinct privileges, roles, capabilities, or rights can be combined in a way that allows an entity to perform unsafe actions that would not be allowed without that combination.

## Related Weaknesses
- ChildOf: CWE-269

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — A user can be given or gain access rights of another user. This can give the user unauthorized access to sensitive information including the access information of another user.

## Potential Mitigations
- [Architecture and Design] Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design, Operation] Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Demonstrative Examples (summary)
- This code allows someone with the role of "ADMIN" or "OPERATOR" to reset a user's password. The role of "OPERATOR" is intended to have less privileges than an "ADMIN", but still be able to help users with small issues such as forgotten passwords.
