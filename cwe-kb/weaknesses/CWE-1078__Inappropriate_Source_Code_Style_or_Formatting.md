# CWE-1078: Inappropriate Source Code Style or Formatting

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1078.html  

## Description
The source code does not follow desired style or formatting for indentation, white space, comments, etc.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Increase Analytical Complexity — Variations in indentation and other white space, comments, etc. can make it more difficult for human analysts to understand the actual behavior that is being implemented.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Static Analysis - Source Code] An Integrated Development Environment (IDE) or linter can report or highlight this weaknesses.

## Demonstrative Examples (summary)
- The usage of symbolic names instead of hard-coded constants is preferred.
