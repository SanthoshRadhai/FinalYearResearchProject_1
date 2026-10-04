# CAPEC-220: Client-Server Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/220.html  

## Description
An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Prerequisites
- The client and/or server must utilize a protocol that has a weakness allowing manipulation of the interaction.

## Resources Required
- The adversary must be able to identify the weakness in the utilized protocol and exploit it. This may require a sniffing tool as well as packet creation abilities. The adversary will be aided if they can force the client and/or server to utilize a specific protocol known to contain exploitable weaknesses.

## Related Weaknesses (CWE)
- CWE-757
