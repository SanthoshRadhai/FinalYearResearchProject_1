# CWE-477: Use of Obsolete Function

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/477.html  

## Description
The code uses deprecated or obsolete functions, which suggests that the code has not been actively reviewed or maintained.

## Extended Description
As programming languages evolve, functions occasionally become obsolete due to: Advances in the language Improved understanding of how operations should be performed effectively and securely Changes in the conventions that govern certain operations Functions that are removed are usually replaced by newer counterparts that perform the same task in some different and hopefully improved way.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Refer to the documentation for the obsolete function in order to determine why it is deprecated or obsolete and to learn about alternative ways to achieve the same functionality.
- [Requirements] Consider seriously the security implications of using an obsolete function. Consider using alternate functions.

## Detection Methods
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Binary / Bytecode Quality Analysis Cost effective for partial coverage: Bytecode Weakness Analysis - including disassembler + source code weakness analysis
- [Manual Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Debugger
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Manual Source Code Review (not inspections) Cost effective for partial coverage: Focused Manual Spotcheck - Focused manual analysis of source
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Source Code Quality Analyzer Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Automated Static Analysis] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Origin Analysis
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- The following code uses the deprecated function getpw() to verify that a plaintext password matches a user's encrypted password. If the password is valid, the function sets result to 1; otherwise it is set to 0.
- In the following code, the programmer assumes that the system always has a property named "cmd" defined. If an attacker can control the program's environment so that "cmd" is not defined, the program throws a null pointer exception when it attempts to call the "Trim()" method.
- The following code constructs a string object from an array of bytes and a value that specifies the top 8 bits of each 16-bit Unicode character.
