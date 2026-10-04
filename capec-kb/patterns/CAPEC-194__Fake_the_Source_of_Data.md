# CAPEC-194: Fake the Source of Data

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/194.html  

## Description
An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simplest forms of this attack would be the creation of an email message with a modified "From" field in order to appear that the message was sent from someone other than the actual sender. The root of the attack (in this case the email system) fails to properly authenticate the source and this results in the reader incorrectly performing the instructed action. Results of the attack vary depending on the details of the attack, but common results include privilege escalation, obfuscation of other attacks, and data corruption/manipulation.

## Related Attack Patterns
- ChildOf: CAPEC-151
- CanPrecede: CAPEC-657
- CanPrecede: CAPEC-667

## Prerequisites
- This attack is only applicable when a vulnerable entity associates data or services with an identity. Without such an association, there would be no reason to fake the source.

## Resources Required
- Resources required vary depending on the nature of the attack. Possible tools needed by an attacker could include tools to create custom network packets, specific client software, and tools to capture network traffic. Many variants of this attack require no attacker resources, however.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic
- Scope: Integrity; Impact: Gain Privileges
- Scope: Integrity; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-287
