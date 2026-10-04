# CAPEC-28: Fuzzing

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/28.html  

## Description
In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds randomly constructed input to the system and looks for an indication that a failure in response to that input has occurred. Fuzzing treats the system as a black box and is totally free from any preconceptions or assumptions about the system. Fuzzing can help an attacker discover certain assumptions made about user input in the system. Fuzzing gives an attacker a quick way of potentially uncovering some of these assumptions despite not necessarily knowing anything about the internals of the system. These assumptions can then be turned against the system by specially crafting user input that may allow an attacker to achieve their goals.

## Skills Required
- [Low] There is a wide variety of fuzzing tools available.

## Resources Required
- Fuzzing tools.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Alter Execution Logic

## Mitigations
- Test to ensure that the software behaves as per specification and that there are no unintended side effects. Ensure that no assumptions about the validity of data are made.
- Use fuzz testing during the software QA process to uncover any surprises, uncover any assumptions or unexpected behavior.

## Related Weaknesses (CWE)
- CWE-74
- CWE-20
