# CAPEC-243: XSS Targeting HTML Attributes

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/243.html  

## Description
An adversary inserts commands to perform cross-site scripting (XSS) actions in HTML attributes. Many filters do not adequately sanitize attributes against the presence of potentially dangerous commands even if they adequately sanitize tags. For example, dangerous expressions could be inserted into a style attribute in an anchor tag, resulting in the execution of malicious code when the resulting page is rendered. If a victim is tricked into viewing the rendered page the attack proceeds like a normal XSS attack, possibly resulting in the loss of sensitive cookies or other malicious activities.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The target application must fail to adequately sanitize HTML attributes against the presence of dangerous commands.

## Resources Required
- The adversary must trick the victim into following a crafted link to a vulnerable server or view a web post where the dangerous commands are executed.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for all input including that which is not expected to have any scripting content.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-83
