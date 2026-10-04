# CAPEC-79: Using Slashes in Alternate Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/79.html  

## Description
This attack targets the encoding of the Slash characters. An adversary would try to exploit common filtering problems related to the use of the slashes characters to gain access to resources on the target host. Directory-driven systems, such as file systems and databases, typically use the slash character to indicate traversal between directories or other container components. For murky historical reasons, PCs (and, as a result, Microsoft OSs) choose to use a backslash, whereas the UNIX world typically makes use of the forward slash. The schizophrenic result is that many MS-based systems are required to understand both forms of the slash. This gives the adversary many opportunities to discover and abuse a number of common filtering problems. The goal of this pattern is to discover server software that only applies filters to one version, but not the other.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application server accepts paths to locate resources.
- The application server does insufficient input data validation on the resource path requested by the user.
- The access right to resources are not set properly.

## Skills Required
- [Low] An adversary can try variation of the slashes characters.
- [Medium] An adversary can use more sophisticated tool or script to scan a website and find a path filtering problem.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process. Refer to the RFCs to safely decode URL.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx)
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- Test your path decoding process against malicious input.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the application based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-173
- CWE-180
- CWE-181
- CWE-20
- CWE-74
- CWE-73
- CWE-22
- CWE-185
- CWE-200
- CWE-697
- CWE-707
