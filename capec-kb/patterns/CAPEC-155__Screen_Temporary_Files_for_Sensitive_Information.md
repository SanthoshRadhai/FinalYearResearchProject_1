# CAPEC-155: Screen Temporary Files for Sensitive Information

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/155.html  

## Description
An adversary exploits the temporary, insecure storage of information by monitoring the content of files used to store temp data during an application's routine execution flow. Many applications use temporary files to accelerate processing or to provide records of state across multiple executions of the application. Sometimes, however, these temporary files may end up storing sensitive information. By screening an application's temporary files, an adversary might be able to discover such sensitive information. For example, web browsers often cache content to accelerate subsequent lookups. If the content contains sensitive information then the adversary could recover this from the web cache.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The target application must utilize temporary files and must fail to adequately secure them against other parties reading them.

## Resources Required
- Because some application may have a large number of temporary files and/or these temporary files may be very large, an adversary may need tools that help them quickly search these files for sensitive information. If the adversary can simply copy the files to another location and if the speed of the search is not important, the adversary can still perform the attack without any special resources.

## Related Weaknesses (CWE)
- CWE-377
