# CAPEC-78: Using Escaped Slashes in Alternate Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/78.html  

## Description
This attack targets the use of the backslash in alternate encoding. An adversary can provide a backslash as a leading character and causes a parser to believe that the next character is special. This is called an escape. By using that trick, the adversary tries to exploit alternate ways to encode the same character which leads to filter problems and opens avenues to attack.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application accepts the backlash character as escape character.
- The application server does incomplete input data decoding, filtering and validation.

## Skills Required
- [Low] The adversary can naively try backslash character and discover that the target host uses it as escape character.
- [Medium] The adversary may need deep understanding of the host target in order to exploit the vulnerability. The adversary may also use automated tools to probe for this vulnerability.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Verify that the user-supplied data does not use backslash character to escape malicious characters.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Be aware of the threat of alternative method of data encoding.
- Regular expressions can be used to filter out backslash. Make sure you decode before filtering and validating the untrusted input data.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.

## Related Weaknesses (CWE)
- CWE-180
- CWE-181
- CWE-173
- CWE-172
- CWE-73
- CWE-22
- CWE-74
- CWE-20
- CWE-697
- CWE-707
