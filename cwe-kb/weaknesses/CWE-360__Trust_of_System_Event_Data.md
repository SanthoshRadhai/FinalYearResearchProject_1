# CWE-360: Trust of System Event Data

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/360.html  

## Description
Security based on event locations are insecure and can be spoofed.

## Extended Description
Events are a messaging system which may provide control data to programs listening for events. Events often do not have any type of authentication framework to allow them to be verified from a trusted source. Any application, in Windows, on a given desktop can send a message to any window on the same desktop. There is no authentication framework for these messages. Therefore, any message can be used to manipulate any process on the desktop if the process does not check the validity and safeness of those messages.

## Related Weaknesses
- ChildOf: CWE-345

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands — If one trusts the system-event information and executes commands based on it, one could potentially take actions based on a spoofed identity.

## Potential Mitigations
- [Architecture and Design] Never trust or rely any of the information in an Event for security.

## Demonstrative Examples (summary)
- This example code prints out secret information when an authorized user activates a button:
