# CAPEC-37: Retrieve Embedded Sensitive Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/37.html  

## Description
An attacker examines a target system to find sensitive data that has been embedded within it. This information can reveal confidential contents, such as account numbers or individual keys/credentials that can be used as an intermediate step in a larger attack.

## Related Attack Patterns
- ChildOf: CAPEC-167

## Prerequisites
- In order to feasibly execute this type of attack, some valuable data must be present in client software.
- Additionally, this information must be unprotected, or protected in a flawed fashion, or through a mechanism that fails to resist reverse engineering, statistical, or other attack.

## Skills Required
- [Medium] The attacker must possess knowledge of client code structure as well as ability to reverse-engineer or decompile it or probe it in other ways. This knowledge is specific to the technology and language used for the client distribution

## Resources Required
- The attacker must possess access to the system or code being exploited. Such access, for this set of attacks, will likely be physical. The attacker will make use of reverse engineering technologies, perhaps for data or to extract functionality from the binary. Such tool use may be as simple as "Strings" or a hex editor. Removing functionality may require the use of only a hex editor, or may require aspects of the toolchain used to construct the application: for instance the Adobe Flash development environment. Attacks of this nature do not require network access or undue CPU, memory, or other hardware-based resources.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Related Weaknesses (CWE)
- CWE-226
- CWE-311
- CWE-525
- CWE-312
- CWE-314
- CWE-315
- CWE-318
- CWE-1239
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1278
- CWE-1301
- CWE-1330
