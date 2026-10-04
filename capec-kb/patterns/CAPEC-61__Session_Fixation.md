# CAPEC-61: Session Fixation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/61.html  

## Description
The attacker induces a client to establish a session with the target software using a session identifier provided by the attacker. Once the user successfully authenticates to the target software, the attacker uses the (now privileged) session identifier in their own transactions. This attack leverages the fact that the target software either relies on client-generated session identifiers or maintains the same session identifiers after privilege elevation.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- Session identifiers that remain unchanged when the privilege levels change.
- Permissive session management mechanism that accepts random user-generated session identifiers
- Predictable session identifiers

## Skills Required
- [Low] Only basic skills are required to determine and fixate session identifiers in a user's browser. Subsequent attacks may require greater skill levels depending on the attackers' motives.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a strict session management mechanism that only accepts locally generated session identifiers: This prevents attackers from fixating session identifiers of their own choice.
- Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- Use session identifiers that are difficult to guess or brute-force: One way for the attackers to obtain valid session identifiers is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.

## Related Weaknesses (CWE)
- CWE-384
- CWE-664
- CWE-732
