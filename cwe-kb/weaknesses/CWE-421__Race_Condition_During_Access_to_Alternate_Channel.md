# CWE-421: Race Condition During Access to Alternate Channel

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/421.html  

## Description
The product opens an alternate channel to communicate with an authorized user, but the channel is accessible to other actors.

## Extended Description
This creates a race condition that allows an attacker to access the channel before the authorized user does.

## Related Weaknesses
- ChildOf: CWE-420
- ChildOf: CWE-362

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism
