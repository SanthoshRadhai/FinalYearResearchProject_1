# CAPEC-501: Android Activity Hijack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/501.html  

## Description
An adversary intercepts an implicit intent sent to launch a Android-based trusted activity and instead launches a counterfeit activity in its place. The malicious activity is then used to mimic the trusted activity's user interface and prompt the target to enter sensitive data as if they were interacting with the trusted activity.

## Related Attack Patterns
- ChildOf: CAPEC-499
- ChildOf: CAPEC-173

## Prerequisites
- The adversary must have previously installed the malicious application onto the Android device that will run in place of the trusted activity.

## Skills Required
- [High] The adversary must typically overcome network and host defenses in order to place malware on the system.

## Resources Required
- Malware capable of acting on the adversary's objectives.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An 'explicit intent' is delivered to a specific application as declared within the intent, whereas an 'implicit intent' is directed to an application as defined by the Android operating system. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly (i.e., with appropriate security controls).
- Never use implicit intents for inter-application communication.

## Related Weaknesses (CWE)
- CWE-923
