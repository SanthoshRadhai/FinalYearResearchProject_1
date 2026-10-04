# CAPEC-143: Detect Unpublicized Web Pages

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/143.html  

## Description
An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain access to information that the targeted site did not intend to make public.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The targeted web site must include pages within its published tree that are not connected to its tree of links. The sensitivity of the content of these pages determines the severity of this attack.

## Resources Required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common page locations from known paths.

## Related Weaknesses (CWE)
- CWE-425
