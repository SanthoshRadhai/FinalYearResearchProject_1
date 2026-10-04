# CAPEC-628: Carry-Off GPS Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/628.html  

## Description
A common form of a GPS spoofing attack, commonly termed a carry-off attack begins with an adversary broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the genuine signals. Over time, the adversary can carry the target away from their intended destination and toward a location chosen by the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-627

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills Required
- [High] This attack requires advanced knoweldge in GPS technology.
