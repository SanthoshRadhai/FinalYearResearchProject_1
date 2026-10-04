# CAPEC-636: Hiding Malicious Data or Code within Files

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/636.html  

## Description
Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail for an image file. Unless utilities are invoked in a particular way, this data is not visible during the normal use of the file. It is possible for an attacker to store malicious data or code using these facilities, which would be difficult to discover.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Prerequisites
- The operating system must support a file system that allows for alternate data storage for a file.

## Mitigations
- Many tools are available to search for the hidden data. Scan regularly for such data using one of these tools.

## Related Weaknesses (CWE)
- CWE-506
