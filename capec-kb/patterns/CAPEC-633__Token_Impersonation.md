# CAPEC-633: Token Impersonation

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/633.html  

## Description
An adversary exploits a weakness in authentication to create an access token (or equivalent) that impersonates a different entity, and then associates a process/thread to that that impersonated token. This action causes a downstream user to make a decision or take action that is based on the assumed identity, and not the response that blocks the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- This pattern of attack is only applicable when a downstream user leverages tokens to verify identity, and then takes action based on that identity.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic
- Scope: Integrity; Impact: Gain Privileges
- Scope: Integrity; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-287
- CWE-1270
