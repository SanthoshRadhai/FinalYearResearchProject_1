# CAPEC-5: Blue Boxing

**Abstraction:** Detailed  
**Status:** Obsolete  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/5.html  

## Description
This type of attack against older telephone switches and trunks has been around for decades. A tone is sent by an adversary to impersonate a supervisor signal which has the effect of rerouting or usurping command of the line. While the US infrastructure proper may not contain widespread vulnerabilities to this type of attack, many companies are connected globally through call centers and business process outsourcing. These international systems may be operated in countries which have not upgraded Telco infrastructure and so are vulnerable to Blue boxing. Blue boxing is a result of failure on the part of the system to enforce strong authorization for administrative functions. While the infrastructure is different than standard current applications like web applications, there are historical lessons to be learned to upgrade the access control for administrative functions. This attack pattern is included in CAPEC for historical purposes.

## Related Attack Patterns
- ChildOf: CAPEC-220

## Prerequisites
- System must use weak authentication mechanisms for administrative functions.

## Skills Required
- [Low] Given a vulnerable phone system, the attackers' technical vector relies on attacks that are well documented in cracker 'zines and have been around for decades.

## Resources Required
- CCITT-5 or other vulnerable lines, with the ability to send tones such as combined 2,400 Hz and 2,600 Hz tones to the switch

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Upgrade phone lines. Note this may be prohibitively expensive
- Use strong access control such as two factor access control for administrative access to the switch

## Related Weaknesses (CWE)
- CWE-285
