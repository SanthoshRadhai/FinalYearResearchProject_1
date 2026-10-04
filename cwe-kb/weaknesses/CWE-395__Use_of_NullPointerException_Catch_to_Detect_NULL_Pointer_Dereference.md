# CWE-395: Use of NullPointerException Catch to Detect NULL Pointer Dereference

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/395.html  

## Description
Catching NullPointerException should not be used as an alternative to programmatic checks to prevent dereferencing a null pointer.

## Extended Description
Programmers typically catch NullPointerException under three circumstances: The program contains a null pointer dereference. Catching the resulting exception was easier than fixing the underlying problem. The program explicitly throws a NullPointerException to signal an error condition. The code is part of a test harness that supplies unexpected input to the classes under test. Of these three circumstances, only the last is acceptable.

## Related Weaknesses
- ChildOf: CWE-705
- ChildOf: CWE-755

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU)

## Potential Mitigations
- [Architecture and Design, Implementation] Do not extensively rely on catching exceptions (especially for validating user input) to handle errors. Handling exceptions can decrease the performance of an application.

## Detection Methods
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Framework-based Fuzzer
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Cost effective for partial coverage: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- The following code mistakenly catches a NullPointerException.
