# CWE-646: Reliance on File Name or Extension of Externally-Supplied File

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/646.html  

## Description
The product allows a file to be uploaded, but it relies on the file name or extension of the file to determine the appropriate behaviors. This could be used by attackers to cause the file to be misclassified and processed in a dangerous fashion.

## Extended Description
An application might use the file name or extension of a user-supplied file to determine the proper course of action, such as selecting the correct process to which control should be passed, deciding what data should be made available, or what resources should be allocated. If the attacker can cause the code to misclassify the supplied file, then the wrong action could occur. For example, an attacker could supply a file that ends in a ".php.gif" extension that appears to be a GIF image, but would be processed as PHP code. In extreme cases, code execution is possible, but the attacker could also cause exhaustion of resources, denial of service, exposure of debug or system data (including application source code), or being bound to a particular server side process. This weakness may be due to a vulnerability in any of the technologies used by the web and application servers, due to misconfiguration, or resultant from another flaw in the application itself.

## Related Weaknesses
- ChildOf: CWE-345
- PeerOf: CWE-434

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — An attacker may be able to read sensitive data.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — An attacker may be able to cause a denial of service.
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — An attacker may be able to gain privileges.

## Potential Mitigations
- [Architecture and Design] Make decisions on the server side based on file content and not on file name or extension.
