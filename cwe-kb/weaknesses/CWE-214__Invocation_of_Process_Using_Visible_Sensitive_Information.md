# CWE-214: Invocation of Process Using Visible Sensitive Information

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/214.html  

## Description
A process is invoked with sensitive command-line arguments, environment variables, or other elements that can be seen by other processes on the operating system.

## Extended Description
Many operating systems allow a user to list information about processes that are owned by other users. Other users could see information such as command line arguments or environment variable settings. When this data contains sensitive information such as credentials, it might allow other users to launch an attack against the product or related resources.

## Related Weaknesses
- ChildOf: CWE-497

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Demonstrative Examples (summary)
- In the example below, the password for a keystore file is read from a system property.
