# CWE-1271: Uninitialized Value on Reset for Registers Holding Security Settings

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1271.html  

## Description
Security-critical logic is not set to a known value on reset.

## Extended Description
When the device is first brought out of reset, the state of registers will be indeterminate if they have not been initialized by the logic. Before the registers are initialized, there will be a window during which the device is in an insecure state and may be vulnerable to attack.

## Related Weaknesses
- ChildOf: CWE-909

## Common Consequences
- Scope: Access Control, Authentication, Authorization; Impact: Varies by Context

## Potential Mitigations
- [Implementation] Design checks should be performed to identify any uninitialized flip-flops used for security-critical functions.
- [Architecture and Design] All registers holding security-critical information should be set to a specific value on reset.

## Demonstrative Examples (summary)
- Shown below is a positive clock edge triggered flip-flop used to implement a lock bit for test and debug interface. When the circuit is first brought out of reset, the state of the flip-flop will be unknown until the enable input and D-input signals update the flip-flop state. In this example, an attacker can reset the device until the test and debug interface is unlocked and access the test interface until the lock signal is driven to a known state by the logic.
