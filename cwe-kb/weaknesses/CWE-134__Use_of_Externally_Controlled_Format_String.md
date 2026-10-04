# CWE-134: Use of Externally-Controlled Format String

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/134.html  

## Description
The product uses a function that accepts a format string as an argument, but the format string originates from an external source.

## Related Weaknesses
- ChildOf: CWE-668
- ChildOf: CWE-668
- CanPrecede: CWE-123
- ChildOf: CWE-20

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory — Format string problems allow for information disclosure which can severely simplify exploitation of the program.
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Memory, Execute Unauthorized Code or Commands — Format string problems can result in the execution of arbitrary code, buffer overflows, denial of service, or incorrect data representation.

## Potential Mitigations
- [Requirements] Choose a language that is not subject to this flaw.
- [Implementation] Ensure that all format string functions are passed a static string which cannot be controlled by the user, and that the proper number of arguments are always sent to that function as well. If at all possible, use functions that do not support the %n operator in format strings. [REF-116] [REF-117]
- [Build and Compilation] Run compilers and linkers with high warning levels, since they may detect incorrect usage.

## Detection Methods
- [Automated Static Analysis] This weakness can often be detected using automated static analysis tools. Many modern tools use data flow analysis or constraint-based techniques to minimize the number of false positives.
- [Black Box] Since format strings often occur in rarely-occurring erroneous conditions (e.g. for error message logging), they can be difficult to detect using black box methods. It is highly likely that many latent issues exist in executables that do not have associated source code (or equivalent source.
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis Cost effective for partial coverage: Binary / Bytecode simple extractor - strings, ELF readers, etc.
- [Manual Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- [Dynamic Analysis with Automated Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Web Application Scanner Web Services Scanner Database Scanners
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Fuzz Tester Framework-based Fuzzer
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Manual Source Code Review (not inspections) Cost effective for partial coverage: Focused Manual Spotcheck - Focused manual analysis of source
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer Cost effective for partial coverage: Warning Flags
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Cost effective for partial coverage: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- The following program prints a string provided as an argument.
- The following code copies a command line argument into a buffer using snprintf().
- Certain implementations make more advanced attacks even easier by providing format directives that control the location in memory to read from or write to. An example of these directives is shown in the following code, written for glibc:
