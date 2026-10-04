# CAPEC-568: Capture Credentials via Keylogger

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/568.html  

## Description
An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystrokes made by a user, the adversary can analyze the data and determine which string are likely to be passwords or other credential related information.

## Related Attack Patterns
- ChildOf: CAPEC-569
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The ability to install the keylogger, either in person or remote.

## Mitigations
- Strong physical security can help reduce the ability of an adversary to install a keylogger.
