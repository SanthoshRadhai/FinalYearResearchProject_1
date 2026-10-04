# CAPEC-252: PHP Local File Inclusion

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/252.html  

## Description
The attacker loads and executes an arbitrary local PHP file on a target machine. The attacker could use this to try to load old versions of PHP files that have known vulnerabilities, to load PHP files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted PHP application must have a bug that allows an attacker to control which code file is loaded at some juncture.

## Resources Required
- The attacker needs to have enough access to the target application to control the identity of a locally included PHP file.

## Related Weaknesses (CWE)
- CWE-829
