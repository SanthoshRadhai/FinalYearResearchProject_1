# CWE-379: Creation of Temporary File in Directory with Insecure Permissions

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/379.html  

## Description
The product creates a temporary file in a directory whose permissions allow unintended actors to determine the file's existence or otherwise access that file.

## Extended Description
On some operating systems, the fact that the temporary file exists may be apparent to any user with sufficient privileges to access that directory. Since the file is visible, the application that is using the temporary file could be known. If one has access to list the processes on the system, the attacker has gained information about what the user is doing at that time. By correlating this with the applications the user is running, an attacker could potentially discover what a user's actions are. From this, higher levels of security could be breached.

## Related Weaknesses
- ChildOf: CWE-377

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Since the file is visible and the application which is using the temp file could be known, the attacker has gained information about what the user is doing at that time.

## Potential Mitigations
- [Requirements] Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.
- [Implementation] Try to store sensitive tempfiles in a directory which is not world readable -- i.e., per-user directories.
- [Implementation] Avoid using vulnerable temp file functions.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code examples a temporary file is created and written to. After using the temporary file, the file is closed and deleted from the file system.
