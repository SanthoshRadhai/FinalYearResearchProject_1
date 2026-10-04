# CAPEC-634: Probe Audio and Video Peripherals

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/634.html  

## Description
The adversary exploits the target system's audio and video functionalities through malware or scheduled tasks. The goal is to capture sensitive information about the target for financial, personal, political, or other gains which is accomplished by collecting communication data between two parties via the use of peripheral devices (e.g. microphones and webcams) or applications with audio and video capabilities (e.g. Skype) on a system.

## Related Attack Patterns
- ChildOf: CAPEC-651
- ChildOf: CAPEC-545

## Prerequisites
- Knowledge of the target device's or application’s vulnerabilities that can be capitalized on with malicious code. The adversary must be able to place the malicious code on the target device.

## Skills Required
- [High] To deploy a hidden process or malware on the system to automatically collect audio and video data.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Prevent unknown code from executing on a system through the use of an allowlist policy.
- Patch installed applications as soon as new updates become available.

## Related Weaknesses (CWE)
- CWE-267
