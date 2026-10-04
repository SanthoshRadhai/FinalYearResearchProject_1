# CWE-703: Improper Check or Handling of Exceptional Conditions

**Abstraction:** Pillar  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/703.html  

## Description
The product does not properly anticipate or handle exceptional conditions that rarely occur during normal operation of the product.

## Common Consequences
- Scope: Confidentiality, Availability, Integrity; Impact: Read Application Data, DoS: Crash, Exit, or Restart, Unexpected State

## Detection Methods
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Fault Injection - source code Fault Injection - binary Cost effective for partial coverage: Forced Path Execution
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Manual Source Code Review (not inspections) Cost effective for partial coverage: Focused Manual Spotcheck - Focused manual analysis of source
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.) Formal Methods / Correct-By-Construction

## Demonstrative Examples (summary)
- Consider the following code segment:
- The following method throws three types of exceptions.
