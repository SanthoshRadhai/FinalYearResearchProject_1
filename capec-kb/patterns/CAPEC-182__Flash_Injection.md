# CAPEC-182: Flash Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/182.html  

## Description
An attacker tricks a victim to execute malicious flash content that executes commands or makes flash calls specified by the attacker. One example of this attack is cross-site flashing, an attacker controlled parameter to a reference call loads from content specified by the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-137
- CanAlsoBe: CAPEC-248

## Prerequisites
- The target must be capable of running Flash applications. In some cases, the victim must follow an attacker-supplied link.

## Skills Required
- [Medium] The attacker needs to have knowledge of Flash, especially how to insert content the executes commands.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The attacker may need to be able to serve the injected Flash content.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: remove sensitive information such as user name and password in the SWF file.
- Implementation: use validation on both client and server side.
- Implementation: remove debug information.
- Implementation: use SSL when loading external data
- Implementation: use crossdomain.xml file to allow the application domain to load stuff or the SWF file called by other domain.

## Related Weaknesses (CWE)
- CWE-20
- CWE-184
- CWE-697
