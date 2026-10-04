# CAPEC-186: Malicious Software Update

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/186.html  

## Description
An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source.

## Related Attack Patterns
- ChildOf: CAPEC-184
- CanFollow: CAPEC-98

## Skills Required
- [High] This attack requires advanced cyber capabilities

## Resources Required
- Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the adversary to host a payload and then trigger the installation of the payload code.

## Consequences
- Scope: Access Control, Availability, Confidentiality; Impact: Execute Unauthorized Commands

## Mitigations
- Validate software updates before installing.

## Related Weaknesses (CWE)
- CWE-494
