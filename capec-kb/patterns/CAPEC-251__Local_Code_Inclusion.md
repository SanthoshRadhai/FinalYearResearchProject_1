# CAPEC-251: Local Code Inclusion

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/251.html  

## Description
The attacker forces an application to load arbitrary code files from the local machine. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-175

## Prerequisites
- The targeted application must have a bug that allows an adversary to control which code file is loaded at some juncture.
- Some variants of this attack may require that old versions of some code files be present and in predictable locations.

## Resources Required
- The adversary needs to have enough access to the target application to control the identity of a locally included file. The attacker may also need to be able to upload arbitrary code files to the target machine, although any location for these files may be acceptable.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Implementation: Avoid passing user input to filesystem or framework API. If necessary to do so, implement a specific, allowlist approach.

## Related Weaknesses (CWE)
- CWE-829
