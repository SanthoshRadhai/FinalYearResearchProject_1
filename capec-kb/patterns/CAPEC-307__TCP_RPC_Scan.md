# CAPEC-307: TCP RPC Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/307.html  

## Description
An adversary scans for RPC services listing on a Unix/Linux host.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- RPC scanning requires no special privileges when it is performed via a native system utility.

## Resources Required
- The ability to craft custom RPC datagrams for use during network reconnaissance via native OS utilities or a port scanning tool. By tailoring the bytes injected one can scan for specific RPC-registered services. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Typically, an IDS/IPS system is very effective against this type of attack.

## Related Weaknesses (CWE)
- CWE-200
