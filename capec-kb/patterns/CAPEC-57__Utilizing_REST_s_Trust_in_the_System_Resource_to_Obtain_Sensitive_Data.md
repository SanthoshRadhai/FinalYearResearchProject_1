# CAPEC-57: Utilizing REST's Trust in the System Resource to Obtain Sensitive Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/57.html  

## Description
This attack utilizes a REST(REpresentational State Transfer)-style applications' trust in the system resources and environment to obtain sensitive data once SSL is terminated.

## Related Attack Patterns
- ChildOf: CAPEC-157

## Prerequisites
- Opportunity to intercept must exist beyond the point where SSL is terminated.
- The adversary must be able to insert a listener actively (proxying the communication) or passively (sniffing the communication) in the client-server communication path.

## Skills Required
- [Low] To insert a network sniffer or other listener into the communication stream

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Implement message level security such as HMAC in the HTTP communication
- Design: Utilize defense in depth, do not rely on a single security mechanism like SSL
- Design: Enforce principle of least privilege

## Related Weaknesses (CWE)
- CWE-300
- CWE-287
- CWE-693
