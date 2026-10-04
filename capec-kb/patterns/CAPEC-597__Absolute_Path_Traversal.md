# CAPEC-597: Absolute Path Traversal

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/597.html  

## Description
An adversary with access to file system resources, either directly or via application logic, will use various file absolute paths and navigation mechanisms such as ".." to extend their range of access to inappropriate areas of the file system. The goal of the adversary is to access directories and files that are intended to be restricted from their access.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- The target must leverage and access an underlying file system.

## Skills Required
- [Low] Simple command line attacks.
- [Medium] Programming attacks.

## Resources Required
- The attacker must have access to an application interface or a direct shell that allows them to inject directory strings and monitor the results.

## Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Configure the access control correctly.
- Design: Enforce principle of least privilege.
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification using an allowlist approach.

## Related Weaknesses (CWE)
- CWE-36
