# CAPEC-36: Using Unpublished Interfaces or Functionality

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/36.html  

## Description
An adversary searches for and invokes interfaces or functionality that the target system designers did not intend to be publicly available. If interfaces fail to authenticate requests, the attacker may be able to invoke functionality they are not authorized for.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The architecture under attack must publish or otherwise make available services that clients can attach to, either in an unauthenticated fashion, or having obtained an authentication token elsewhere. The service need not be 'discoverable', but in the event it isn't it must have some way of being discovered by an attacker. This might include listening on a well-known port. Ultimately, the likelihood of exploit depends on discoverability of the vulnerable service.

## Skills Required
- [Low] A number of web service digging tools are available for free that help discover exposed web services and their interfaces. In the event that a web service is not listed, the attacker does not need to know much more in addition to the format of web service messages that they can sniff/monitor for.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Web service digging tools may be helpful.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Authenticating both services and their discovery, and protecting that authentication mechanism simply fixes the bulk of this problem. Protecting the authentication involves the standard means, including: 1) protecting the channel over which authentication occurs, 2) preventing the theft, forgery, or prediction of authentication credentials or the resultant tokens, or 3) subversion of password reset and the like.

## Related Weaknesses (CWE)
- CWE-306
- CWE-693
- CWE-695
- CWE-1242
