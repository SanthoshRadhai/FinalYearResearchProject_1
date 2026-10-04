# CWE-749: Exposed Dangerous Method or Function

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/749.html  

## Description
The product provides an Applications Programming Interface (API) or similar interface for interaction with external actors, but the interface includes a dangerous method or function that is not properly restricted.

## Extended Description
This weakness can lead to a wide variety of resultant weaknesses, depending on the behavior of the exposed method. It can apply to any number of technologies and approaches, such as ActiveX controls, Java functions, IOCTLs, and so on. The exposure can occur in a few different ways: The function/method was never intended to be exposed to outside actors. The function/method was only intended to be accessible to a limited set of actors, such as Internet-based access from a single web site.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Access Control, Other; Impact: Gain Privileges or Assume Identity, Read Application Data, Modify Application Data, Execute Unauthorized Code or Commands, Other — Exposing critical functionality essentially provides an attacker with the privilege level of the exposed functionality. This could result in the modification or exposure of sensitive data or possibly even execution of arbitrary code.

## Potential Mitigations
- [Architecture and Design] If you must expose a method, make sure to perform input validation on all arguments, limit access to authorized parties, and protect against all possible vulnerabilities.
- [Architecture and Design, Implementation] Identify all exposed functionality. Explicitly list all functionality that must be exposed to some user or set of users. Identify which functionality may be: accessible to all users restricted to a small set of privileged users prevented from being directly accessible at all Ensure that the implemented code follows these expectations. This includes setting the appropriate access modifiers where applicable (public, private, protected, etc.) or not marking ActiveX controls safe-for-scripting.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java example the method removeDatabase will delete the database with the name specified in the input parameter.
- These Android and iOS applications intercept URL loading within a WebView and perform special actions if a particular URL scheme is used, thus allowing the Javascript within the WebView to communicate with the application:
- This application uses a WebView to display websites, and creates a Javascript interface to a Java object to allow enhanced functionality on a trusted website:
- After Android 4.2, only methods annotated with @JavascriptInterface are available in JavaScript, protecting usage of getClass() by default, as in this example:
