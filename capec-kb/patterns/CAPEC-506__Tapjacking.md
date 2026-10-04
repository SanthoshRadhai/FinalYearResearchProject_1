# CAPEC-506: Tapjacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/506.html  

## Description
An adversary, through a previously installed malicious application, displays an interface that misleads the user and convinces them to tap on an attacker desired location on the screen. This is often accomplished by overlaying one screen on top of another while giving the appearance of a single interface. There are two main techniques used to accomplish this. The first is to leverage transparent properties that allow taps on the screen to pass through the visible application to an application running in the background. The second is to strategically place a small object (e.g., a button or text field) on top of the visible screen and make it appear to be a part of the underlying application. In both cases, the user is convinced to tap on the screen but does not realize the application that they are interacting with.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- This pattern of attack requires the ability to execute a malicious application on the user's device. This malicious application is used to present the interface to the user and make the attack possible.

## Related Weaknesses (CWE)
- CWE-1021
