# CAPEC-564: Run Software at Logon

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/564.html  

## Description
Operating system allows logon scripts to be run whenever a specific user or users logon to a system. If adversaries can access these scripts, they may insert additional code into the logon script. This code can allow them to maintain persistence or move laterally within an enclave because it is executed every time the affected user or users logon to a computer. Modifying logon scripts can effectively bypass workstation and enclave firewalls. Depending on the access configuration of the logon scripts, either local credentials or a remote administrative account may be necessary.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Restrict write access to logon scripts to necessary administrators.

## Related Weaknesses (CWE)
- CWE-284
