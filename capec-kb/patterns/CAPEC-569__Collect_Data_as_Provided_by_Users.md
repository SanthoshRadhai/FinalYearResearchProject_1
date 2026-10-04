# CAPEC-569: Collect Data as Provided by Users

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/569.html  

## Description
An attacker leverages a tool, device, or program to obtain specific information as provided by a user of the target system. This information is often needed by the attacker to launch a follow-on attack. This attack is different than Social Engineering as the adversary is not tricking or deceiving the user. Instead the adversary is putting a mechanism in place that captures the information that a user legitimately enters into a system. Deploying a keylogger, performing a UAC prompt, or wrapping the Windows default credential provider are all examples of such interactions.

## Related Attack Patterns
- ChildOf: CAPEC-116
