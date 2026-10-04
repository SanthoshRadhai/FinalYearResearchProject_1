# CAPEC-74: Manipulating State

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/74.html  

## Description
The adversary modifies state information maintained by the target software or causes a state transition in hardware. If successful, the target will use this tainted state and execute in an unintended manner. State management is an important function within a software application. User state maintained by the application can include usernames, payment information, browsing history as well as application-specific contents such as items in a shopping cart. Manipulating user state can be employed by an adversary to elevate privilege, conduct fraudulent transactions or otherwise modify the flow of the application to derive certain benefits. If there is a hardware logic error in a finite state machine, the adversary can use this to put the system in an undefined state which could cause a denial of service or exposure of secure data.

## Prerequisites
- User state is maintained at least in some way in user-controllable locations, such as cookies or URL parameters.
- There is a faulty finite state machine in the hardware logic that can be exploited.

## Skills Required
- [Medium] The adversary needs to have knowledge of state management as employed by the target application, and also the ability to manipulate the state in a meaningful way.

## Resources Required
- The adversary needs a data tampering tool capable of generating and creating custom inputs to aid in the attack, like Fiddler, Wireshark, or a similar in-browser plugin (e.g., Tamper Data for Firefox).

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Do not rely solely on user-controllable locations, such as cookies or URL parameters, to maintain user state.
- Avoid sensitive information, such as usernames or authentication and authorization information, in user-controllable locations.
- Sensitive information that is part of the user state must be appropriately protected to ensure confidentiality and integrity at each request.
- All possible states must be handled by hardware finite state machines.

## Related Weaknesses (CWE)
- CWE-372
- CWE-315
- CWE-353
- CWE-693
- CWE-1245
- CWE-1253
- CWE-1265
- CWE-1271
