# CAPEC-101: Server Side Include (SSI) Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/101.html  

## Description
An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.

## Related Attack Patterns
- ChildOf: CAPEC-253
- CanPrecede: CAPEC-600

## Prerequisites
- A web server that supports server side includes and has them enabled
- User controllable input that can carry include directives to the web server

## Skills Required
- [Medium] The attacker needs to be aware of SSI technology, determine the nature of injection and be able to craft input that results in the SSI directives being executed.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Determining whether the server supports SSI does not require special tools, and nor does injecting directives that get executed. Spidering tools can make the task of finding and following links easier.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them
- All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive
- Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead

## Related Weaknesses (CWE)
- CWE-97
- CWE-74
- CWE-20
