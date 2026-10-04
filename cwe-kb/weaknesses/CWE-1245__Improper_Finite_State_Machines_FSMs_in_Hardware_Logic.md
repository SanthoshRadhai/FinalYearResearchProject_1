# CWE-1245: Improper Finite State Machines (FSMs) in Hardware Logic

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1245.html  

## Description
Faulty finite state machines (FSMs) in the hardware logic allow an attacker to put the system in an undefined state, to cause a denial of service (DoS) or gain privileges on the victim's system.

## Extended Description
The functionality and security of the system heavily depend on the implementation of FSMs. FSMs can be used to indicate the current security state of the system. Lots of secure data operations and data transfers rely on the state reported by the FSM.

## Related Weaknesses
- ChildOf: CWE-684

## Common Consequences
- Scope: Availability, Access Control; Impact: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Instability, Gain Privileges or Assume Identity — Faulty FSM designs that do not account for all states, either through undefined states (left as don't cares) or through incorrect implementation, might lead an attacker to drive the system into an unstable state from which the system cannot recover without a reset, thus causing a DoS. Depending on what the FSM is used for, an attacker might also gain additional privileges to launch further attacks and compromise the security guarantees.

## Potential Mitigations
- [Architecture and Design, Implementation] Define all possible states and handle all unused states through default statements. Ensure that system defaults to a secure state.

## Demonstrative Examples (summary)
- The Finite State Machine (FSM) shown in the "bad" code snippet below assigns the output ("out") based on the value of state, which is determined based on the user provided input ("user_input").
