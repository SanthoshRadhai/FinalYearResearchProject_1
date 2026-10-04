# CAPEC-383: Harvesting Information via API Event Monitoring

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/383.html  

## Description
An adversary hosts an event within an application framework and then monitors the data exchanged during the course of the event for the purpose of harvesting any important data leaked during the transactions. One example could be harvesting lists of usernames or userIDs for the purpose of sending spam messages to those users. One example of this type of attack involves the adversary creating an event within the sub-application. Assume the adversary hosts a "virtual sale" of rare items. As other users enter the event, the attacker records via AiTM (CAPEC-94) proxy the user_ids and usernames of everyone who attends. The adversary would then be able to spam those users within the application using an automated script.

## Related Attack Patterns
- ChildOf: CAPEC-407
- CanPrecede: CAPEC-94

## Prerequisites
- The target software is utilizing application framework APIs

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Leverage encryption techniques during information transactions so as to protect them from attack patterns of this kind.

## Related Weaknesses (CWE)
- CWE-311
- CWE-319
- CWE-419
- CWE-602
