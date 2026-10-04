# CAPEC-13: Subverting Environment Variable Values

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/13.html  

## Description
The adversary directly or indirectly modifies environment variables used by or controlling the target software. The adversary's goal is to cause the target software to deviate from its expected operation in a manner that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-77
- CanPrecede: CAPEC-14
- PeerOf: CAPEC-10

## Prerequisites
- An environment variable is accessible to the user.
- An environment variable used by the application can be tainted with user supplied data.
- Input data used in an environment variable is not validated properly.
- The variables encapsulation is not done properly. For instance setting a variable as public in a class makes it visible and an adversary may attempt to manipulate that variable.

## Skills Required
- [Low] In a web based scenario, the client controls the data that it submitted to the server. So anybody can try to send malicious data and try to bypass the authentication mechanism.
- [High] Some more advanced attacks may require knowledge about protocols and probing technique which help controlling a variable. The malicious user may try to understand the authentication mechanism in order to defeat it.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability; Impact: Hide Activities

## Mitigations
- Protect environment variables against unauthorized read and write access.
- Protect the configuration files which contain environment variables against illegitimate read and write access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Apply the least privilege principles. If a process has no legitimate reason to read an environment variable do not give that privilege.

## Related Weaknesses (CWE)
- CWE-353
- CWE-285
- CWE-302
- CWE-74
- CWE-15
- CWE-73
- CWE-20
- CWE-200
