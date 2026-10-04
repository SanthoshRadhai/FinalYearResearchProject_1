# CAPEC-191: Read Sensitive Constants Within an Executable

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/191.html  

## Description
An adversary engages in activities to discover any sensitive constants present within the compiled code of an executable. These constants may include literal ASCII strings within the file itself, or possibly strings hard-coded into particular routines that can be revealed by code refactoring methods including static and dynamic analysis.

## Related Attack Patterns
- ChildOf: CAPEC-167

## Prerequisites
- Access to a binary or executable such that it can be analyzed by various utilities.

## Resources Required
- Binary analysis programs such as 'strings' or 'grep', or hex editors.

## Related Weaknesses (CWE)
- CWE-798
