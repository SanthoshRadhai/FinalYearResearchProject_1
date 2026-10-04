# CWE-540: Inclusion of Sensitive Information in Source Code

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/540.html  

## Description
Source code on a web server or repository often contains sensitive information and should generally not be accessible to users.

## Extended Description
There are situations where it is critical to remove source code from an area or server. For example, obtaining Perl source code on a system allows an attacker to understand the logic of the script and extract extremely useful information such as code bugs or logins and passwords.

## Related Weaknesses
- ChildOf: CWE-538

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design, System Configuration] Recommendations include removing this script from the web server and moving it to a location not accessible from the Internet.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code uses an include file to store database credentials:
- The following comment, embedded in a JSP, will be displayed in the resulting HTML output.
