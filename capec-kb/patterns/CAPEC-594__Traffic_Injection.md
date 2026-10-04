# CAPEC-594: Traffic Injection

**Abstraction:** Meta  
**Status:** Stable  
**Reference:** https://capec.mitre.org/data/definitions/594.html  

## Description
An adversary injects traffic into the target's network connection. The adversary is therefore able to degrade or disrupt the connection, and potentially modify the content. This is not a flooding attack, as the adversary is not focusing on exhausting resources. Instead, the adversary is crafting a specific input to affect the system in a particular way.

## Prerequisites
- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Resources Required
- A tool, such as a MITM Proxy, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Other

## Related Weaknesses (CWE)
- CWE-940
