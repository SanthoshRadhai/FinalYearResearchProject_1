# CAPEC-267: Leverage Alternate Encoding

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/267.html  

## Description
An adversary leverages the possibility to encode potentially harmful input or content used by applications such that the applications are ineffective at validating this encoding standard.

## Related Attack Patterns
- ChildOf: CAPEC-153

## Prerequisites
- The application's decoder accepts and interprets encoded characters. Data canonicalization, input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills Required
- [Low] An adversary can inject different representation of a filtered character in a different encoding.
- [Medium] An adversary may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Related Weaknesses (CWE)
- CWE-173
- CWE-172
- CWE-180
- CWE-181
- CWE-73
- CWE-74
- CWE-20
- CWE-697
- CWE-692
