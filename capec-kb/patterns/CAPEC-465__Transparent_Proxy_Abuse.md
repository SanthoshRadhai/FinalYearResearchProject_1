# CAPEC-465: Transparent Proxy Abuse

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/465.html  

## Description
A transparent proxy serves as an intermediate between the client and the internet at large. It intercepts all requests originating from the client and forwards them to the correct location. The proxy also intercepts all responses to the client and forwards these to the client. All of this is done in a manner transparent to the client.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- Transparent proxy is usedVulnerable configuration of network topology involving the transparent proxy (e.g., no NAT happening between the client and the proxy)Execution of malicious Flash or Applet in the victim's browser

## Skills Required
- [Medium] Creating malicious Flash or Applet to open a cross-domain socket connection to a remote system

## Mitigations
- Design: Ensure that the transparent proxy uses an actual network layer IP address for routing requests. On the transparent proxy, disable the use of routing based on address information in the HTTP host header.
- Configuration: Disable in the browser the execution of Java Script, Flash, SilverLight, etc.

## Related Weaknesses (CWE)
- CWE-441
