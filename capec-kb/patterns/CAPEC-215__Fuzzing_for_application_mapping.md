# CAPEC-215: Fuzzing for application mapping

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/215.html  

## Description
An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash.

## Related Attack Patterns
- ChildOf: CAPEC-54
- ChildOf: CAPEC-28

## Prerequisites
- The target application must fail to sanitize incoming messages adequately before processing.

## Skills Required
- [Medium] Although fuzzing parameters is not difficult, and often possible with automated fuzzing tools, interpreting the error conditions and modifying the parameters so as to move further in the process of mapping the application requires detailed knowledge of target platform, the languages and packages used as well as software design.

## Resources Required
- Fuzzing tools, which automatically generate and send message variants, are necessary for this attack. The attacker must have sufficient access to send messages to the target. The attacker must also have the ability to observe the target application's log and/or error messages in order to collect information about the target.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.
- Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Obfuscate database type in Database API's error message.

## Related Weaknesses (CWE)
- CWE-209
- CWE-532
