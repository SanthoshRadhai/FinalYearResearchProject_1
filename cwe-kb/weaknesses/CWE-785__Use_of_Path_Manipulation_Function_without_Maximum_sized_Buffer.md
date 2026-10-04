# CWE-785: Use of Path Manipulation Function without Maximum-sized Buffer

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/785.html  

## Description
The product invokes a function for normalizing paths or file names, but it provides an output buffer that is smaller than the maximum possible size, such as PATH_MAX.

## Extended Description
Passing an inadequately-sized output buffer to a path manipulation function can result in a buffer overflow. Such functions include realpath(), readlink(), PathAppend(), and others.

## Related Weaknesses
- ChildOf: CWE-676
- ChildOf: CWE-120
- ChildOf: CWE-20

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Memory, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Potential Mitigations
- [Implementation] Always specify output buffers large enough to handle the maximum-size possible result from path manipulation functions.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example the function creates a directory named "output\<name>" in the current directory and returns a heap-allocated copy of its name.
