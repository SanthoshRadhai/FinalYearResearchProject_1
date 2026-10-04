# CAPEC-129: Pointer Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/129.html  

## Description
This attack pattern involves an adversary manipulating a pointer within a target application resulting in the application accessing an unintended memory location. This can result in the crashing of the application or, for certain pointer values, access to data that would not normally be possible or the execution of arbitrary code. Since pointers are simply integer variables, Integer Attacks may often be used in Pointer Attacks.

## Prerequisites
- The target application must have a pointer variable that the attacker can influence to hold an arbitrary value.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-682
- CWE-822
- CWE-823
