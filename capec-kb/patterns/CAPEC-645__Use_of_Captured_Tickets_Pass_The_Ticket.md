# CAPEC-645: Use of Captured Tickets (Pass The Ticket)

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/645.html  

## Description
An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. An adversary can obtain any one of these tickets (e.g. Service Ticket, Ticket Granting Ticket, Silver Ticket, or Golden Ticket) to authenticate to a system/resource without needing the account's credentials. Depending on the ticket obtained, the adversary may be able to access a particular resource or generate TGTs for any account within an Active Directory Domain.

## Related Attack Patterns
- ChildOf: CAPEC-652
- CanPrecede: CAPEC-151

## Prerequisites
- The adversary needs physical access to the victim system.
- The use of a third-party credential harvesting tool.

## Skills Required
- [Low] Determine if Kerberos authentication is used on the server.
- [High] The adversary uses a third-party tool to obtain the necessary tickets to execute the attack.

## Consequences
- Scope: Integrity; Impact: Gain Privileges

## Mitigations
- Reset the built-in KRBTGT account password twice to invalidate the existence of any current Golden Tickets and any tickets derived from them.
- Monitor system and domain logs for abnormal access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-294
- CWE-308
