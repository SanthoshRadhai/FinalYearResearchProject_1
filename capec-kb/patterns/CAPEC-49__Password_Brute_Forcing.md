# CAPEC-49: Password Brute Forcing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/49.html  

## Description
An adversary tries every possible value for a password until they succeed. A brute force attack, if feasible computationally, will always be successful because it will essentially go through all possible passwords given the alphabet used (lower case letters, upper case letters, numbers, symbols, etc.) and the maximum length of the password.

## Related Attack Patterns
- ChildOf: CAPEC-112
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- An adversary needs to know a username to target.
- The system uses password based authentication as the one factor authentication mechanism.
- An application does not have a password throttling mechanism in place. A good password throttling mechanism will make it almost impossible computationally to brute force a password as it may either lock out the user after a certain number of incorrect attempts or introduce time out periods. Both of these would make a brute force attack impractical.

## Skills Required
- [Low] A brute force attack is very straightforward. A variety of password cracking tools are widely available.

## Resources Required
- A powerful enough computer for the job with sufficient CPU, RAM and HD. Exact requirements will depend on the size of the brute force job and the time requirement for completion. Some brute forcing jobs may require grid or distributed computing (e.g. DES Challenge).

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-257
- CWE-654
- CWE-307
- CWE-308
- CWE-309
