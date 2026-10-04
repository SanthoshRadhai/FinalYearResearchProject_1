# CAPEC-216: Communication Channel Manipulation

**Abstraction:** Meta  
**Status:** Stable  
**Reference:** https://capec.mitre.org/data/definitions/216.html  

## Description
An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.

## Related Attack Patterns
- CanPrecede: CAPEC-94

## Prerequisites
- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Resources Required
- A tool that is capable of viewing network traffic and generating custom inputs to be used in the attack.

## Consequences
- Scope: Integrity; Impact: Read Data, Modify Data, Other
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encrypt all sensitive communications using properly-configured cryptography.
- Design the communication system such that it associates proper authentication/authorization with each channel/message.

## Related Weaknesses (CWE)
- CWE-306
