# CAPEC-52: Embedding NULL Bytes

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/52.html  

## Description
An adversary embeds one or more null bytes in input to the target software. This attack relies on the usage of a null-valued byte as a string terminator in many environments. The goal is for certain components of the target software to stop processing the input when it encounters the null byte(s).

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The program does not properly handle postfix NULL terminators

## Skills Required
- [Medium] Directory traversal
- [High] Execution of arbitrary code

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Properly handle the NULL characters supplied as part of user input prior to doing anything with the data.

## Related Weaknesses (CWE)
- CWE-158
- CWE-172
- CWE-173
- CWE-74
- CWE-20
- CWE-697
- CWE-707
