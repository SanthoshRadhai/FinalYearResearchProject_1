# CWE-940: Improper Verification of Source of a Communication Channel

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/940.html  

## Description
The product establishes a communication channel to handle an incoming request that has been initiated by an actor, but it does not properly verify that the request is coming from the expected origin.

## Extended Description
When an attacker can successfully establish a communication channel from an untrusted origin, the attacker may be able to gain privileges and access unexpected functionality.

## Related Weaknesses
- ChildOf: CWE-923
- ChildOf: CWE-346

## Common Consequences
- Scope: Access Control, Other; Impact: Gain Privileges or Assume Identity, Varies by Context, Bypass Protection Mechanism — An attacker can access any functionality that is inadvertently accessible to the source.

## Potential Mitigations
- [Architecture and Design] Use a mechanism that can validate the identity of the source, such as a certificate, and validate the integrity of data to ensure that it cannot be modified in transit using an Adversary-in-the-Middle (AITM) attack. When designing functionality of actions in the URL scheme, consider whether the action should be accessible to all mobile applications, or if an allowlist of applications to interface with is appropriate.

## Demonstrative Examples (summary)
- This Android application will remove a user account when it receives an intent to do so:
- These Android and iOS applications intercept URL loading within a WebView and perform special actions if a particular URL scheme is used, thus allowing the Javascript within the WebView to communicate with the application:
