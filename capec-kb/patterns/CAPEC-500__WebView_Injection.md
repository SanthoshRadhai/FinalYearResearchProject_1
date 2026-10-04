# CAPEC-500: WebView Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/500.html  

## Description
An adversary, through a previously installed malicious application, injects code into the context of a web page displayed by a WebView component. Through the injected code, an adversary is able to manipulate the DOM tree and cookies of the page, expose sensitive information, and can launch attacks against the web application from within the web page.

## Related Attack Patterns
- ChildOf: CAPEC-253

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the device and convince the user to execute it. The malicious application is designed to target a specific web application and is used to load the target web pages via the WebView component. For example, an adversary may develop an application that interacts with Facebook via WebView and adds a new feature that a user desires. The user would install this 3rd party app instead of the Facebook app.

## Mitigations
- The only known mitigation to this type of attack is to keep the malicious application off the system. There is nothing that can be done to the target application to protect itself from a malicious application that has been installed and executed.

## Related Weaknesses (CWE)
- CWE-749
- CWE-940
