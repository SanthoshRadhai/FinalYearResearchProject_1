# CAPEC-55: Rainbow Table Password Cracking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/55.html  

## Description
An attacker gets access to the database table where hashes of passwords are stored. They then use a rainbow table of pre-computed hash chains to attempt to look up the original password. Once the original password corresponding to the hash is obtained, the attacker uses the original password to gain access to the system.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- Hash of the original password is available to the attacker. For a better chance of success, an attacker should have more than one hash of the original password, and ideally the whole table.
- Salt was not used to create the hash of the original password. Otherwise the rainbow tables have to be re-computed, which is very expensive and will make the attack effectively infeasible (especially if salt was added in iterations).
- The system uses one factor password based authentication.

## Skills Required
- [Low] A variety of password cracking tools are available that can leverage a rainbow table. The more difficult part is to obtain the password hash(es) in the first place.

## Resources Required
- Rainbow table of password hash chains with the right algorithm used. A password cracking tool that leverages this rainbow table will also be required. Hash(es) of the password is required.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use salt when computing password hashes. That is, concatenate the salt (random bits) with the original password prior to hashing it.

## Related Weaknesses (CWE)
- CWE-261
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-916
- CWE-308
- CWE-309
