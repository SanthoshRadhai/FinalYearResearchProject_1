# CAPEC-64: Using Slashes and URL Encoding Combined to Bypass Validation Logic

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/64.html  

## Description
This attack targets the encoding of the URL combined with the encoding of the slash characters. An attacker can take advantage of the multiple ways of encoding a URL and abuse the interpretation of the URL. A URL may contain special character that need special syntax handling in order to be interpreted. Special characters are represented using a percentage character followed by two digits representing the octet code of the original character (%HEX-CODE). For instance US-ASCII space character would be represented with %20. This is often referred as escaped ending or percent-encoding. Since the server decodes the URL from the requests, it may restrict the access to some URL paths by validating and filtering out the URL requests it received. An attacker will try to craft an URL with a sequence of special characters which once interpreted by the server will be equivalent to a forbidden URL. It can be difficult to protect against this attack since the URL can contain other format of encoding such as UTF-8 encoding, Unicode-encoding, etc.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills Required
- [Low] An attacker can try special characters in the URL and bypass the URL validation.
- [Medium] The attacker may write a script to defeat the input filtering mechanism.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Related Weaknesses (CWE)
- CWE-177
- CWE-173
- CWE-172
- CWE-73
- CWE-22
- CWE-74
- CWE-20
- CWE-697
- CWE-707
