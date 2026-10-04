# CAPEC-133: Try All Common Switches

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/133.html  

## Description
An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal sensitive processing or configuration information to an attacker. This attack differs from other forms of API abuse in that the attacker is indiscriminately attempting to invoke options in the hope that one of them will work rather than specifically targeting a known option. Nonetheless, even if the attacker is familiar with the published options of a targeted application this attack method may still be fruitful as it might discover unpublicized functionality.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The attacker must be able to control the options or switches sent to the target.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to send requests to the target.

## Mitigations
- Design: Minimize switch and option functionality to only that necessary for correct function of the command.
- Implementation: Remove all debug and testing options from production code.

## Related Weaknesses (CWE)
- CWE-912
