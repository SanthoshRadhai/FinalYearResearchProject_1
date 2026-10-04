# CAPEC-16: Dictionary-based Password Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/16.html  

## Description
An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern. Dictionary Attacks differ from similar attacks such as Password Spraying (CAPEC-565) and Credential Stuffing (CAPEC-600), since they leverage unknown username/password combinations and don't care about inducing account lockouts.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system uses one factor password based authentication.
- The system does not have a sound password policy that is being enforced.
- The system does not implement an effective password throttling mechanism.

## Skills Required
- [Low] A variety of password cracking tools and dictionaries are available to launch this type of an attack.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD). Applicable dictionaries are required. Also a password cracking tool or a custom script that leverages the dictionary database to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-307
- CWE-308
- CWE-309
