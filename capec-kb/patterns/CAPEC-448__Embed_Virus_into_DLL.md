# CAPEC-448: Embed Virus into DLL

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/448.html  

## Description
An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for performance gains. The embedded virus then attempts to infect any machine which interfaces with the product, and possibly steal private data or eavesdrop.

## Related Attack Patterns
- ChildOf: CAPEC-442

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related Weaknesses (CWE)
- CWE-506
