# CAPEC-86: XSS Through HTTP Headers

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/86.html  

## Description
An adversary exploits web applications that generate web content, such as links in a HTML page, based on unvalidated or improperly validated data submitted by other actors. XSS in HTTP Headers attacks target the HTTP headers which are hidden from most users and may not be validated by web applications.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-588
- ChildOf: CAPEC-592

## Prerequisites
- Target software must be a client that allows scripting communication from remote hosts.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an adversary can simply edit HTTP Headers that are sent to client machine.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Resources Required
- The adversary must have the ability to deploy a custom hostile service for access by targeted clients and the abbility to communicate synchronously or asynchronously with client machine. The adversary must also control a remote site of some sort to redirect client and data to.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related Weaknesses (CWE)
- CWE-80
