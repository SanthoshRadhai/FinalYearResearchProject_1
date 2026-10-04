# CAPEC-469: HTTP DoS

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/469.html  

## Description
An attacker performs flooding at the HTTP level to bring down only a particular web application rather than anything listening on a TCP/IP connection. This denial of service attack requires substantially fewer packets to be sent which makes DoS harder to detect. This is an equivalent of SYN flood in HTTP. The idea is to keep the HTTP session alive indefinitely and then repeat that hundreds of times. This attack targets resource depletion weaknesses in web server software. The web server will wait to attacker's responses on the initiated HTTP sessions while the connection threads are being exhausted.

## Related Attack Patterns
- ChildOf: CAPEC-227

## Prerequisites
- HTTP protocol is usedWeb server used is vulnerable to denial of service via HTTP flooding

## Resources Required
- Ability to issues hundreds of HTTP requests

## Mitigations
- Configuration: Configure web server software to limit the waiting period on opened HTTP sessions
- Design: Use load balancing mechanisms

## Related Weaknesses (CWE)
- CWE-770
- CWE-772
