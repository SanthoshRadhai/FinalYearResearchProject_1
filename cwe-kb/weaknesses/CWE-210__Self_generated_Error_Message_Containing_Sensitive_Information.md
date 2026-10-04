# CWE-210: Self-generated Error Message Containing Sensitive Information

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/210.html  

## Description
The product identifies an error condition and creates its own diagnostic or error messages that contain sensitive information.

## Related Weaknesses
- ChildOf: CWE-209

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Implementation, Build and Compilation] Debugging information should not make its way into a production release.
- [Implementation, Build and Compilation] Debugging information should not make its way into a production release.

## Demonstrative Examples (summary)
- The following code uses custom configuration files for each user in the application. It checks to see if the file exists on the system before attempting to open and use the file. If the configuration file does not exist, then an error is generated, and the application exits.
