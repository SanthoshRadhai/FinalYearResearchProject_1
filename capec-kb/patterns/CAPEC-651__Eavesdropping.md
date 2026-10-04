# CAPEC-651: Eavesdropping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/651.html  

## Description
An adversary intercepts a form of communication (e.g. text, audio, video) by way of software (e.g., microphone and audio recording application), hardware (e.g., recording equipment), or physical means (e.g., physical proximity). The goal of eavesdropping is typically to gain unauthorized access to sensitive information about the target for financial, personal, political, or other gains. Eavesdropping is different from a sniffing attack as it does not take place on a network-based communication channel (e.g., IP traffic). Instead, it entails listening in on the raw audio source of a conversation between two or more parties.

## Related Attack Patterns
- ChildOf: CAPEC-117

## Prerequisites
- The adversary typically requires physical proximity to the target's environment, whether for physical eavesdropping or for placing recording equipment. This is not always the case for software-based eavesdropping, if the adversary has the capability to install malware on the target system that can activate a microphone and record audio digitally.

## Resources Required
- For logical eavesdropping, some equipment may be necessary (e.g., microphone, tape recorder, etc.). For physical eavesdropping, only proximity is required.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Be mindful of your surroundings when discussing sensitive information in public areas.
- Implement proper software restriction policies to only allow authorized software on your environment. Use of anti-virus and other security monitoring and detecting tools can aid in this too. Closely monitor installed software for unusual behavior or activity, and implement patches as soon as they become available.
- If possible, physically disable the microphone on your machine if it is not needed.

## Related Weaknesses (CWE)
- CWE-200
