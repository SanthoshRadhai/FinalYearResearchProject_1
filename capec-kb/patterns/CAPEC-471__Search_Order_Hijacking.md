# CAPEC-471: Search Order Hijacking

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/471.html  

## Description
An adversary exploits a weakness in an application's specification of external libraries to exploit the functionality of the loader where the process loading the library searches first in the same directory in which the process binary resides and then in other directories. Exploitation of this preferential search order can allow an attacker to make the loading process load the adversary's rogue library rather than the legitimate library. This attack can be leveraged with many different libraries and with many different loading processes. No forensic trails are left in the system's registry or file system that an incorrect library had been loaded.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- Attacker has a mechanism to place its malicious libraries in the needed location on the file system.

## Skills Required
- [Medium] Ability to create a malicious library.

## Mitigations
- Design: Fix the Windows loading process to eliminate the preferential search order by looking for DLLs in the precise location where they are expected
- Design: Sign system DLLs so that unauthorized DLLs can be detected.

## Related Weaknesses (CWE)
- CWE-427
