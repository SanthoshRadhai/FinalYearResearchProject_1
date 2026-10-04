# CAPEC-175: Code Inclusion

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/175.html  

## Description
An adversary exploits a weakness on the target to force arbitrary code to be retrieved locally or from a remote location and executed. This differs from code injection in that code injection involves the direct inclusion of code while code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Prerequisites
- The target application must include external code/libraries that are executed when the application runs and the adversary must be able to influence the specific files that get included.
- The victim must run the targeted application, possibly using the crafted parameters that the adversary uses to identify the code to include.

## Resources Required
- The adversary may need the capability to host code modules if they wish their own code files to be included.

## Related Weaknesses (CWE)
- CWE-829
