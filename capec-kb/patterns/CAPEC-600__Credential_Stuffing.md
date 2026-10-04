# CAPEC-600: Credential Stuffing

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/600.html  

## Description
An adversary tries known username/password combinations against different systems, applications, or services to gain additional authenticated access. Credential Stuffing attacks rely upon the fact that many users leverage the same username/password combination for multiple systems, applications, and services.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-653

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills Required
- [Low] A Credential Stuffing attack is very straightforward.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- A known list of username/password combinations.
- A custom script that leverages the credential list to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-307
- CWE-308
- CWE-309
- CWE-262
- CWE-263
- CWE-654
