# CAPEC-73: User-Controlled Filename

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/73.html  

## Description
An attack of this type involves an adversary inserting malicious characters (such as a XSS redirection) into a filename, directly or indirectly that is then used by the target software to generate HTML text or other potentially executable content. Many websites rely on user-generated content and dynamically build resources like files, filenames, and URL links directly from user supplied data. In this attack pattern, the attacker uploads code that can execute in the client browser and/or redirect the client browser to a site that the attacker owns. All XSS attack payload variants can be used to pass and exploit these vulnerabilities.

## Related Attack Patterns
- ChildOf: CAPEC-165
- CanPrecede: CAPEC-592

## Prerequisites
- The victim must trust the name and locale of user controlled filenames.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an attacker can simply edit data that the host uses to build the filename
- [Medium] Deploying a malicious "look-a-like" site (such as a site masquerading as a bank or online auction site) that the user enters their authentication data into.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Scan dynamically generated content against validation specification

## Related Weaknesses (CWE)
- CWE-20
- CWE-184
- CWE-96
- CWE-348
- CWE-116
- CWE-350
- CWE-86
- CWE-697
