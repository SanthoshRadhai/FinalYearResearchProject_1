# CAPEC-23: File Content Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/23.html  

## Description
An adversary poisons files with a malicious payload (targeting the file systems accessible by the target software), which may be passed through by standard channels such as via email, and standard web content like PDF and multimedia files. The adversary exploits known vulnerabilities or handling routines in the target processes, in order to exploit the host's trust in executing remote content, including binary files.

## Related Attack Patterns
- ChildOf: CAPEC-242
- CanAlsoBe: CAPEC-165

## Prerequisites
- The target software must consume files.
- The adversary must have access to modify files that the target software will consume.

## Skills Required
- [Medium] How to poison a file with malicious payload that will exploit a vulnerability when the file is opened. The adversary must also know how to place the file onto a system where it will be opened by an unsuspecting party, or force the file to be opened.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Enforce principle of least privilege
- Design: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Implementation: Virus scanning on host
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.

## Related Weaknesses (CWE)
- CWE-20
