# CAPEC-595: Connection Reset

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/595.html  

## Description
In this attack pattern, an adversary injects a connection reset packet to one or both ends of a target's connection. The attacker is therefore able to have the target and/or the destination server sever the connection without having to directly filter the traffic between them.

## Related Attack Patterns
- ChildOf: CAPEC-594

## Prerequisites
- This attack requires the ability to monitor the target's network connection.

## Related Weaknesses (CWE)
- CWE-940
