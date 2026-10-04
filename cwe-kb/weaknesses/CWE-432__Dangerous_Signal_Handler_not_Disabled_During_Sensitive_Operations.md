# CWE-432: Dangerous Signal Handler not Disabled During Sensitive Operations

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/432.html  

## Description
The product uses a signal handler that shares state with other signal handlers, but it does not properly mask or prevent those signal handlers from being invoked while the original signal handler is still running.

## Extended Description
During the execution of a signal handler, it can be interrupted by another handler when a different signal is sent. If the two handlers share state - such as global variables - then an attacker can corrupt the state by sending another signal before the first handler has completed execution.

## Related Weaknesses
- ChildOf: CWE-364

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data

## Potential Mitigations
- [Implementation] Turn off dangerous handlers when performing sensitive operations.
