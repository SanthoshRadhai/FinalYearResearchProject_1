# CAPEC-498: Probe iOS Screenshots

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/498.html  

## Description
An adversary examines screenshot images created by iOS in an attempt to obtain sensitive information. This attack targets temporary screenshots created by the underlying OS while the application remains open in the background.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- This type of an attack requires physical access to a device to either excavate the image files (potentially by leveraging a Jailbreak) or view the screenshots through the multitasking switcher (by double tapping the home button on the device).

## Mitigations
- To mitigate this type of an attack, an application that may display sensitive information should clear the screen contents before a screenshot is taken. This can be accomplished by setting the key window's hidden property to YES. This code to hide the contents should be placed in both the applicationWillResignActive() and applicationDidEnterBackground() methods.

## Related Weaknesses (CWE)
- CWE-359
