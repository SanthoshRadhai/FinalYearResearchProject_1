# CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/93.html  

## Description
The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.

## Related Weaknesses
- ChildOf: CWE-74
- CanPrecede: CWE-117

## Common Consequences
- Scope: Integrity; Impact: Modify Application Data

## Potential Mitigations
- [Implementation] Avoid using CRLF as a special sequence.
- [Implementation] Appropriately filter or quote CRLF sequences in user-controlled input.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code segment reads the name of the author of a weblog entry, author, from an HTTP request and sets it in a cookie header of an HTTP response.
- The following code is a workflow job written using YAML. The code attempts to download pull request artifacts, unzip from the artifact called pr.zip and extract the value of the file NR into a variable "pr_number" that will be used later in another job. It attempts to create a github workflow environment variable, writing to $GITHUB_ENV. The environment variable value is retrieved from an external resource.
- If user input data that eventually makes it to a log message isn't checked for CRLF characters, it may be possible for an attacker to forge entries in a log file.
