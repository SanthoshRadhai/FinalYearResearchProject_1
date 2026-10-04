# CAPEC-41: Using Meta-characters in E-mail Headers to Inject Malicious Payloads

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/41.html  

## Description
This type of attack involves an attacker leveraging meta-characters in email headers to inject improper behavior into email programs. Email software has become increasingly sophisticated and feature-rich. In addition, email applications are ubiquitous and connected directly to the Web making them ideal targets to launch and propagate attacks. As the user demand for new functionality in email applications grows, they become more like browsers with complex rendering and plug in routines. As more email functionality is included and abstracted from the user, this creates opportunities for attackers. Virtually all email applications do not list email header information by default, however the email header contains valuable attacker vectors for the attacker to exploit particularly if the behavior of the email client application is known. Meta-characters are hidden from the user, but can contain scripts, enumerations, probes, and other attacks against the user's system.

## Related Attack Patterns
- ChildOf: CAPEC-242
- ChildOf: CAPEC-134

## Prerequisites
- This attack targets most widely deployed feature rich email applications, including web based email programs.

## Skills Required
- [Low] To distribute email

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Perform validation on email header data
- Implementation: Implement email filtering solutions on mail server or on MTA, relay server.
- Implementation: Mail servers that perform strict validation may catch these attacks, because metacharacters are not allowed in many header variables such as dns names

## Related Weaknesses (CWE)
- CWE-150
- CWE-88
- CWE-697
