# CWE-307: Improper Restriction of Excessive Authentication Attempts

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/307.html  

## Description
The product does not implement sufficient measures to prevent multiple failed authentication attempts within a short time frame.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-287
- ChildOf: CWE-799

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — An attacker could perform an arbitrary number of authentication attempts using different passwords, and eventually gain access to the targeted account using a brute force attack.

## Potential Mitigations
- [Architecture and Design] Common protection mechanisms include: Disconnecting the user after a small number of failed attempts Implementing a timeout Locking out a targeted account Requiring a computational task on the user's part.
- [Architecture and Design] Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Consider using libraries with authentication capabilities such as OpenSSL or the ESAPI Authenticator. [REF-45]

## Detection Methods
- [Dynamic Analysis with Automated Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Web Application Scanner Web Services Scanner Database Scanners Cost effective for partial coverage: Host-based Vulnerability Scanners - Examine configuration for flaws, verifying that audit mechanisms work, ensure host configuration meets certain predefined criteria
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Fuzz Tester Framework-based Fuzzer Cost effective for partial coverage: Forced Path Execution
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Automated Static Analysis] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Configuration Checker
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Cost effective for partial coverage: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- In January 2009, an attacker was able to gain administrator access to a Twitter server because the server did not restrict the number of login attempts [REF-236]. The attacker targeted a member of Twitter's support team and was able to successfully guess the member's password using a brute force attack by guessing a large number of common words. After gaining access as the member of the support staff, the attacker used the administrator panel to gain access to 33 accounts that belonged to celebrities and politicians. Ultimately, fake Twitter messages were sent that appeared to come from the compromised accounts.
- The following code, extracted from a servlet's doPost() method, performs an authentication lookup every time the servlet is invoked.
- This code attempts to limit the number of login attempts by causing the process to sleep before completing the authentication.
- In the following C/C++ example the validateUser method opens a socket connection, reads a username and password from the socket and attempts to authenticate the username and password.
- Consider this example from a real-world attack against the iPhone [REF-1218]. An attacker can use brute force methods; each time there is a failed guess, the attacker quickly cuts the power before the failed entry is recorded, effectively bypassing the intended limit on the number of failed authentication attempts. Note that this attack requires removal of the cell phone battery and connecting directly to the phone's power source, and the brute force attack is still time-consuming.
