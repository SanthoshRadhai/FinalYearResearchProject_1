# CAPEC-139: Relative Path Traversal

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/139.html  

## Description
An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or \) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- The target application must accept a string as user input, fail to sanitize combinations of characters in the input that have a special meaning in the context of path navigation, and insert the user-supplied string into path navigation commands.

## Skills Required
- [Low] To inject the malicious payload in a web page
- [High] To bypass non trivial filters in the application

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.
- Implementation: Prefer working without user input when using file system calls
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.

## Related Weaknesses (CWE)
- CWE-23
