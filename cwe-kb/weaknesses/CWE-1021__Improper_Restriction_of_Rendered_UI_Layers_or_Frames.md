# CWE-1021: Improper Restriction of Rendered UI Layers or Frames

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1021.html  

## Description
The web application does not restrict or incorrectly restricts frame objects or UI layers that belong to another application or domain.

## Related Weaknesses
- ChildOf: CWE-441
- ChildOf: CWE-610
- ChildOf: CWE-451

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data — An attacker can trick a user into performing actions that are masked and hidden from the user's view. The impact varies widely, depending on the functionality of the underlying application. For example, in a social media application, clickjacking could be used to trick the user into changing privacy settings.

## Potential Mitigations
- [Implementation] The use of X-Frame-Options allows developers of web content to restrict the usage of their application within the form of overlays, frames, or iFrames. The developer can indicate from which domains can frame the content. The concept of X-Frame-Options is well documented, but implementation of this protection mechanism is in development to cover gaps. There is a need for allowing frames from multiple domains.
- [Implementation] A developer can use a "frame-breaker" script in each page that should not be framed. This is very helpful for legacy browsers that do not support X-Frame-Options security feature previously mentioned. It is also important to note that this tactic has been circumvented or bypassed. Improper usage of frames can persist in the web application through nested frames. The "frame-breaking" script does not intuitively account for multiple nested frames that can be presented to the user.
- [Implementation] This defense-in-depth technique can be used to prevent the improper usage of frames in web applications. It prioritizes the valid sources of data to be loaded into the application through the usage of declarative policies. Based on which implementation of Content Security Policy is in use, the developer should use the "frame-ancestors" directive or the "frame-src" directive to mitigate this weakness. Both directives allow for the placement of restrictions when it comes to allowing embedded content.
- [Implementation] In addition to frames or iframes as previously mentioned, the web application is expected to place restrictions on whether it is allowed to be rendered within objects, embed, or applet elements.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
