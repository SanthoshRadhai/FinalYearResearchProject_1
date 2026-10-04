# CWE-489: Active Debug Code

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/489.html  

## Description
The product is released with debugging code still enabled or active.

## Related Weaknesses
- ChildOf: CWE-710
- CanPrecede: CWE-215

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control, Other; Impact: Bypass Protection Mechanism, Read Application Data, Gain Privileges or Assume Identity, Varies by Context — Active debug code can create unintended entry points or expose sensitive information. The severity of the exposed debug code will depend on the particular instance. At the least, it will give an attacker sensitive information about the settings and mechanics of web applications on the server. At worst, as is often the case, the debug code will allow an attacker complete control over the web application and server, as well as confidential information that either of these access.

## Potential Mitigations
- [Build and Compilation, Distribution] Remove debug code before deploying the application.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Debug code can be used to bypass authentication. For example, suppose an application has a login script that receives a username and a password. Assume also that a third, optional, parameter, called "debug", is interpreted by the script as requesting a switch to debug mode, and that when this parameter is given the username and password are not checked. In such a case, it is very simple to bypass the authentication process if the special behavior of the application regarding the debug parameter is known. In a case where the form is:
