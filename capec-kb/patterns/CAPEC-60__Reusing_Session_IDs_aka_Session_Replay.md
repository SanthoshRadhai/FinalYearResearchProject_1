# CAPEC-60: Reusing Session IDs (aka Session Replay)

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/60.html  

## Description
This attack targets the reuse of valid session ID to spoof the target system in order to gain privileges. The attacker tries to reuse a stolen session ID used previously during a transaction to perform spoofing and session hijacking. Another name for this type of attack is Session Replay.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are not well protected from session theft.

## Skills Required
- [Low] If an attacker can steal a valid session ID, they can then try to be authenticated with that stolen session ID.
- [Medium] More sophisticated attack can be used to hijack a valid session from a user and spoof a legitimate user by reusing their valid session ID.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Always invalidate a session ID after the user logout.
- Setup a session time out for the session IDs.
- Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate adversary in the middle attacks (CAPEC-94).
- Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.
- Encrypt the session data associated with the session ID.
- Use multifactor authentication.

## Related Weaknesses (CWE)
- CWE-294
- CWE-290
- CWE-346
- CWE-384
- CWE-488
- CWE-539
- CWE-200
- CWE-285
- CWE-664
- CWE-732
