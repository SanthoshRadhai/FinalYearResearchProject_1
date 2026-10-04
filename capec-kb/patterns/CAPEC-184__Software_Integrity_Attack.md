# CAPEC-184: Software Integrity Attack

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/184.html  

## Description
An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of software code, device data structures, or device firmware, achieving the modification of the target's integrity to achieve an insecure state.

## Skills Required
- [Medium] Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the attacker to host a payload and then trigger the installation of the payload code.

## Resources Required
- Software Integrity Attacks are usually a late stage focus of attack activity which depends upon the success of a chain of prior events. The resources required to perform the attack vary with respect to the overall attack strategy, existing countermeasures which must be bypassed, and the success of early phase attack vectors.

## Related Weaknesses (CWE)
- CWE-494
