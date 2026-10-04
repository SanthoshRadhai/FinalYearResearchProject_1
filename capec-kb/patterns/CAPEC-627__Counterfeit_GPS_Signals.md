# CAPEC-627: Counterfeit GPS Signals

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/627.html  

## Description
An adversary attempts to deceive a GPS receiver by broadcasting counterfeit GPS signals, structured to resemble a set of normal GPS signals. These spoofed signals may be structured in such a way as to cause the receiver to estimate its position to be somewhere other than where it actually is, or to be located where it is but at a different time, as determined by the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-148

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills Required
- [High] The ability to spoof GPS signals is not trival.

## Resources Required
- Ability to create spoofed GPS signals.

## Consequences
- Scope: Integrity; Impact: Modify Data
