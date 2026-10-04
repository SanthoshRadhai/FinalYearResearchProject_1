# CAPEC-144: Detect Unpublicized Web Services

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/144.html  

## Description
An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous since unpublished but available services may not have adequate security controls placed upon them given that an administrator may believe they are unreachable.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The targeted web site must include unpublished services within its web tree. The nature of these services determines the severity of this attack.

## Resources Required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common service queries from known paths.

## Related Weaknesses (CWE)
- CWE-425
