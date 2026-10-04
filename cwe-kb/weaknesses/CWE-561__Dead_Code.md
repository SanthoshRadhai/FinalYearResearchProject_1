# CWE-561: Dead Code

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/561.html  

## Description
The product contains dead code, which can never be executed.

## Extended Description
Dead code is code that can never be executed in a running program. The surrounding code makes it impossible for a section of code to ever be executed.

## Related Weaknesses
- ChildOf: CWE-1164

## Common Consequences
- Scope: Other; Impact: Quality Degradation — Dead code that results from code that can never be executed is an indication of problems with the source code that needs to be fixed and is an indication of poor quality.
- Scope: Other; Impact: Reduce Maintainability

## Potential Mitigations
- [Implementation] Remove dead code before deploying the application.

## Detection Methods
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction Cost effective for partial coverage: Attack Modeling
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Binary / Bytecode Quality Analysis Compare binary / bytecode to application permission manifest
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Automated Monitored Execution
- [Automated Static Analysis] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Permission Manifest Analysis
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Source Code Quality Analyzer Cost effective for partial coverage: Warning Flags Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Dynamic Analysis with Automated Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Web Application Scanner Web Services Scanner Database Scanners
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Manual Source Code Review (not inspections) Cost effective for partial coverage: Focused Manual Spotcheck - Focused manual analysis of source

## Demonstrative Examples (summary)
- The condition for the second if statement is impossible to satisfy. It requires that the variables be non-null. However, on the only path where s can be assigned a non-null value, there is a return statement.
- In the following class, two private methods call each other, but since neither one is ever invoked from anywhere else, they are both dead code.
- The field named glue is not used in the following class. The author of the class has accidentally put quotes around the field name, transforming it into a string constant.
