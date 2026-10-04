# CAPEC-560: Use of Known Domain Credentials

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/560.html  

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate credentials (e.g. userID/password) to achieve authentication and to perform authorized actions under the guise of an authenticated user or service.

## Related Attack Patterns
- CanPrecede: CAPEC-151

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills Required
- [Low] Once an adversary obtains a known credential, leveraging it is trivial.

## Resources Required
- A list of known credentials.
- A custom script that leverages the credential list to launch an attack.

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
- CWE-1273
