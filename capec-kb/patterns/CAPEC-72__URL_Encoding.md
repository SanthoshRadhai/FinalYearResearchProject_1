# CAPEC-72: URL Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/72.html  

## Description
This attack targets the encoding of the URL. An adversary can take advantage of the multiple way of encoding an URL and abuse the interpretation of the URL.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application should accepts and decodes URL input.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills Required
- [Low] An adversary can try special characters in the URL and bypass the URL validation.
- [Medium] The adversary may write a script to defeat the input filtering mechanism.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.

## Related Weaknesses (CWE)
- CWE-173
- CWE-177
- CWE-172
- CWE-73
- CWE-74
- CWE-20
