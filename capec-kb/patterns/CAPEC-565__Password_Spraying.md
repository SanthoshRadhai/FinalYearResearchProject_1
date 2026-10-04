# CAPEC-565: Password Spraying

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/565.html  

## Description
In a Password Spraying attack, an adversary tries a small list (e.g. 3-5) of common or expected passwords, often matching the target's complexity policy, against a known list of user accounts to gain valid credentials. The adversary tries a particular password for each user account, before moving onto the next password in the list. This approach assists the adversary in remaining undetected by avoiding rapid or frequent account lockouts. The adversary may then reattempt the process with additional passwords, once enough time has passed to prevent inducing a lockout.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system/application uses one factor password based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts on the target system/application.

## Skills Required
- [Low] A Password Spraying attack is very straightforward. A variety of password cracking tools are widely available.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- Applicable password lists.
- A password cracking tool or a custom script that leverages the password list to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-307
- CWE-308
- CWE-309
