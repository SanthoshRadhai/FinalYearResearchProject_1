# CAPEC-53: Postfix, Null Terminate, and Backslash

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/53.html  

## Description
If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks for a trailing slash character. If a string insertion is possible, but the slash must exist, an alternate encoding of NULL in mid-string may be used.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- Null terminators are not properly handled by the filter.

## Skills Required
- [Medium] An adversary needs to understand alternate encodings, what the filter looks for and the data format acceptable to the target API

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Properly handle Null characters. Make sure canonicalization is properly applied. Do not pass Null characters to the underlying APIs.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-158
- CWE-172
- CWE-173
- CWE-74
- CWE-20
- CWE-697
- CWE-707
