# CWE-625: Permissive Regular Expression

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/625.html  

## Description
The product uses a regular expression that does not sufficiently restrict the set of allowed values.

## Extended Description
This effectively causes the regexp to accept substrings that match the pattern, which produces a partial comparison to the target. In some cases, this can lead to other weaknesses. Common errors include: not identifying the beginning and end of the target string using wildcards instead of acceptable character ranges others

## Related Weaknesses
- ChildOf: CWE-185
- PeerOf: CWE-187
- PeerOf: CWE-184
- PeerOf: CWE-183

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Implementation] When applicable, ensure that the regular expression marks beginning and ending string patterns, such as "/^string$/" for Perl.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code takes phone numbers as input, and uses a regular expression to reject invalid phone numbers.
- This code uses a regular expression to validate an IP string prior to using it in a call to the "ping" command.
