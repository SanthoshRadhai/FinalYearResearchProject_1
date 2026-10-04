# CWE-378: Creation of Temporary File With Insecure Permissions

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/378.html  

## Description
Opening temporary files without appropriate measures or controls can leave the file, its contents and any function that it impacts vulnerable to attack.

## Related Weaknesses
- ChildOf: CWE-377

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — If the temporary file can be read by the attacker, sensitive information may be in that file which could be revealed.
- Scope: Authorization, Other; Impact: Other — If that file can be written to by the attacker, the file might be moved into a place to which the attacker does not have access. This will allow the attacker to gain selective resource access-control privileges.
- Scope: Integrity, Other; Impact: Other — Depending on the data stored in the temporary file, there is the potential for an attacker to gain an additional input vector which is trusted as non-malicious. It may be possible to make arbitrary changes to data structures, user information, or even process ownership.

## Potential Mitigations
- [Requirements] Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.
- [Implementation] Ensure that you use proper file permissions. This can be achieved by using a safe temp file function. Temporary files should be writable and readable only by the process that owns the file.
- [Implementation] Randomize temporary file names. This can also be achieved by using a safe temp-file function. This will ensure that temporary files will not be created in predictable places.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code examples a temporary file is created and written to. After using the temporary file, the file is closed and deleted from the file system.
