# CAPEC-71: Using Unicode Encoding to Bypass Validation Logic

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/71.html  

## Description
An attacker may provide a Unicode string to a system component that is not Unicode aware and use that to circumvent the filter or cause the classifying mechanism to fail to properly understanding the request. That may allow the attacker to slip malicious data past the content filter and/or possibly cause the application to route the request incorrectly.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- Filtering is performed on data that has not be properly canonicalized.

## Skills Required
- [Medium] An attacker needs to understand Unicode encodings and have an idea (or be able to find out) what system components may not be Unicode aware.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Ensure that the system is Unicode aware and can properly process Unicode data. Do not make an assumption that data will be in ASCII.
- Ensure that filtering or input validation is applied to canonical data.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-176
- CWE-179
- CWE-180
- CWE-173
- CWE-172
- CWE-184
- CWE-183
- CWE-74
- CWE-20
- CWE-697
- CWE-692
