# CAPEC-70: Try Common or Default Usernames and Passwords

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/70.html  

## Description
An adversary may try certain common or default usernames and passwords to gain access into the system and perform unauthorized actions. An adversary may try an intelligent brute force using empty passwords, known vendor default credentials, as well as a dictionary of common usernames and passwords. Many vendor products come preconfigured with default (and thus well-known) usernames and passwords that should be deleted prior to usage in a production environment. It is a common mistake to forget to remove these default login credentials. Another problem is that users would pick very simple (common) passwords (e.g. "secret" or "password") that make it easier for the attacker to gain access to the system compared to using a brute force attack or even a dictionary attack using a full dictionary.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system uses one factor password based authentication.The adversary has the means to interact with the system.

## Skills Required
- [Low] An adversary just needs to gain access to common default usernames/passwords specific to the technologies used by the system. Additionally, a brute force attack leveraging common passwords can be easily realized if the user name is known.

## Resources Required
- Technology or vendor specific list of default usernames and passwords.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Delete all default account credentials that may be put in by the product vendor.
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-798
- CWE-654
- CWE-308
- CWE-309
