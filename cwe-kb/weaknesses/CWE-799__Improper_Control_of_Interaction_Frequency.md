# CWE-799: Improper Control of Interaction Frequency

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/799.html  

## Description
The product does not properly limit the number or frequency of interactions that it has with an actor, such as the number of incoming requests.

## Extended Description
This can allow the actor to perform actions more frequently than expected. The actor could be a human or an automated process such as a virus or bot. This could be used to cause a denial of service, compromise program logic (such as limiting humans to a single vote), or other consequences. For example, an authentication routine might not limit the number of times an attacker can guess a password. Or, a web site might conduct a poll but only expect humans to vote a maximum of once a day.

## Related Weaknesses
- ChildOf: CWE-691

## Common Consequences
- Scope: Availability, Access Control, Other; Impact: DoS: Resource Consumption (Other), Bypass Protection Mechanism, Other

## Demonstrative Examples (summary)
- In the following code a username and password is read from a socket and an attempt is made to authenticate the username and password. The code will continuously checked the socket for a username and password until it has been authenticated.
