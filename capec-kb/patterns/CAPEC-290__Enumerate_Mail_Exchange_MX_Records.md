# CAPEC-290: Enumerate Mail Exchange (MX) Records

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/290.html  

## Description
An adversary enumerates the MX records for a given via a DNS query. This type of information gathering returns the names of mail servers on the network. Mail servers are often not exposed to the Internet but are located within the DMZ of a network protected by a firewall. A side effect of this configuration is that enumerating the MX records for an organization my reveal the IP address of the firewall or possibly other internal systems. Attackers often resort to MX record enumeration when a DNS Zone Transfer is not possible.

## Related Attack Patterns
- ChildOf: CAPEC-309

## Prerequisites
- The adversary requires access to a DNS server that will return the MX records for a network.

## Resources Required
- A command-line utility or other application capable of sending requests to the DNS server is necessary.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200
