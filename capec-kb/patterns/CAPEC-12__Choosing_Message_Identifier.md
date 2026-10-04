# CAPEC-12: Choosing Message Identifier

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/12.html  

## Description
This pattern of attack is defined by the selection of messages distributed via multicast or public information channels that are intended for another client by determining the parameter value assigned to that client. This attack allows the adversary to gain access to potentially privileged information, and to possibly perpetrate other attacks through the distribution means by impersonation. If the channel/message being manipulated is an input rather than output mechanism for the system, (such as a command bus), this style of attack could be used to change the adversary's identifier to more a privileged one.

## Related Attack Patterns
- PeerOf: CAPEC-21
- ChildOf: CAPEC-216

## Prerequisites
- Information and client-sensitive (and client-specific) data must be present through a distribution channel available to all users.
- Distribution means must code (through channel, message identifiers, or convention) message destination in a manner visible within the distribution means itself (such as a control channel) or in the messages themselves.

## Skills Required
- [Low] All the adversary needs to discover is the format of the messages on the channel/distribution means and the particular identifier used within the messages.

## Resources Required
- The adversary needs the ability to control source code or application configuration responsible for selecting which message/channel id is absorbed from the public distribution means.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Associate some ACL (in the form of a token) with an authenticated user which they provide middleware. The middleware uses this token as part of its channel/message selection for that client, or part of a discerning authorization decision for privileged channels/messages. The purpose is to architect the system in a way that associates proper authentication/authorization with each channel/message.
- Re-architect system input/output channels as appropriate to distribute self-protecting data. That is, encrypt (or otherwise protect) channels/messages so that only authorized readers can see them.

## Related Weaknesses (CWE)
- CWE-201
- CWE-306
