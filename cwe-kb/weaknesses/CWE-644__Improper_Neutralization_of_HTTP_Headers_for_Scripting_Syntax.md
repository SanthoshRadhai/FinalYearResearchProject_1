# CWE-644: Improper Neutralization of HTTP Headers for Scripting Syntax

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/644.html  

## Description
The product does not neutralize or incorrectly neutralizes web scripting syntax in HTTP headers that can be used by web browser components that can process raw headers, such as Flash.

## Extended Description
An attacker may be able to conduct cross-site scripting and other attacks against users who have these components enabled. If a product does not neutralize user controlled data being placed in the header of an HTTP response coming from the server, the header may contain a script that will get executed in the client's browser context, potentially resulting in a cross site scripting vulnerability or possibly an HTTP response splitting attack. It is important to carefully control data that is being placed both in HTTP response header and in the HTTP response body to ensure that no scripting syntax is present, taking various encodings into account.

## Related Weaknesses
- ChildOf: CWE-116

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — Run arbitrary code.
- Scope: Confidentiality; Impact: Read Application Data — Attackers may be able to obtain sensitive information.

## Potential Mitigations
- [Architecture and Design] Perform output validation in order to filter/escape/encode unsafe data that is being passed from the server in an HTTP response header.
- [Architecture and Design] Disable script execution functionality in the clients' browser.

## Demonstrative Examples (summary)
- In the following Java example, user-controlled data is added to the HTTP headers and returned to the client. Given that the data is not subject to neutralization, a malicious user may be able to inject dangerous scripting tags that will lead to script execution in the client browser.
