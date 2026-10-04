# CAPEC-635: Alternative Execution Due to Deceptive Filenames

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/635.html  

## Description
The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be able to execute malicious code, cause a denial of service or expose sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Prerequisites
- The use of the file must be controlled by the file extension.

## Mitigations
- Applications should insure that the content of the file is consistent with format it is expecting, and not depend solely on the file extension.

## Related Weaknesses (CWE)
- CWE-162
