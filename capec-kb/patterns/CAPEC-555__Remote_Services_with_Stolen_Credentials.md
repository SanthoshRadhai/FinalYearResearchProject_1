# CAPEC-555: Remote Services with Stolen Credentials

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/555.html  

## Description
This pattern of attack involves an adversary that uses stolen credentials to leverage remote services such as RDP, telnet, SSH, and VNC to log into a system. Once access is gained, any number of malicious activities could be performed.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151

## Mitigations
- Disable RDP, telnet, SSH and enable firewall rules to block such traffic. Limit users and accounts that have remote interactive login access. Remove the Local Administrators group from the list of groups allowed to login through RDP. Limit remote user permissions. Use remote desktop gateways and multifactor authentication for remote logins.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521
