# CAPEC-150: Collect Data from Common Resource Locations

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/150.html  

## Description
An adversary exploits well-known locations for resources for the purposes of undermining the security of the target. In many, if not most systems, files and resources are organized in a default tree structure. This can be useful for adversaries because they often know where to look for resources or files that are necessary for attacks. Even when the precise location of a targeted resource may not be known, naming conventions may indicate a small area of the target machine's file tree where the resources are typically located. For example, configuration files are normally stored in the /etc director on Unix systems. Adversaries can take advantage of this to commit other types of attacks.

## Related Attack Patterns
- ChildOf: CAPEC-116

## Prerequisites
- The targeted applications must either expect files to be located at a specific location or, if the location of the files can be configured by the user, the user either failed to move the files from the default location or placed them in a conventional location for files of the given type.

## Resources Required
- None: No specialized resources are required to execute this type of attack. In some cases, the attacker need not even have direct access to the locations on the target computer where the targeted resources reside.

## Related Weaknesses (CWE)
- CWE-552
- CWE-1239
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1323
- CWE-1330
