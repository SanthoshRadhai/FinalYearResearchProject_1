# CAPEC-598: DNS Spoofing

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/598.html  

## Description
An adversary sends a malicious ("NXDOMAIN" ("No such domain") code, or DNS A record) response to a target's route request before a legitimate resolver can. This technique requires an On-path or In-path device that can monitor and respond to the target's DNS requests. This attack differs from BGP Tampering in that it directly responds to requests made by the target instead of polluting the routing the target's infrastructure uses.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- On/In Path Device

## Skills Required
- [Low] To distribute email

## Mitigations
- Design: Avoid dependence on DNS
- Design: Include "hosts file"/IP address in the application
- Implementation: Utilize a .onion domain with Tor support
- Implementation: DNSSEC
- Implementation: DNS-hold-open
