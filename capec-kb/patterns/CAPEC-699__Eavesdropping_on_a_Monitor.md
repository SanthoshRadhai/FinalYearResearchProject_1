# CAPEC-699: Eavesdropping on a Monitor

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/699.html  

## Description
An Adversary can eavesdrop on the content of an external monitor through the air without modifying any cable or installing software, just capturing this signal emitted by the cable or video port, with this the attacker will be able to impact the confidentiality of the data without being detected by traditional security tools

## Related Attack Patterns
- ChildOf: CAPEC-651

## Prerequisites
- Victim should use an external monitor device
- Physical access to the target location and devices

## Skills Required
- [Medium] Knowledge of how to use the SDR and related software: With this knowledge, the adversary will find the correct frequency where the signal is being leaked
- [Low] Understanding of computing hardware, to identify the video cable and video ports

## Resources Required
- SDR device set with the correspondent antenna
- Computer with SDR Software

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Enhance: Increase the number of electromagnetic shield layers in the display ports and cables to contain or reduce the intensity of the leaked signal.
- Implement: Use a protocol that encrypts the video signal; in case the signal is intercepted the signal is protected by the encryption.
- Design: Lock away the video cables, making it difficult for the attacker to access the cables and place the antenna near them (If the distance condition between the antenna and display port/cable is not satisfied, the attack will not be possible).
- Implement: Use wireless technologies to connect to external display devices.

## Related Weaknesses (CWE)
- CWE-1300
