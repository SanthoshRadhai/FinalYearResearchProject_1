# CAPEC-545: Pull Data from System Resources

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/545.html  

## Description
An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necessarily know what they are going to find when they start pulling data. This is different than CAPEC-150 where the adversary knows what they are looking for due to the common location.

## Related Attack Patterns
- ChildOf: CAPEC-116

## Related Weaknesses (CWE)
- CWE-1239
- CWE-1243
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1278
- CWE-1323
- CWE-1258
- CWE-1330
