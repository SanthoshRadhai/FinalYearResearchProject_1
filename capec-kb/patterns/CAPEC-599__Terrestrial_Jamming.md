# CAPEC-599: Terrestrial Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/599.html  

## Description
In this attack pattern, the adversary transmits disruptive signals in the direction of the target's consumer-level satellite dish (as opposed to the satellite itself). The transmission disruption occurs in a more targeted range. Portable terrestrial jammers have a range of 3-5 kilometers in urban areas and 20 kilometers in rural areas. This technique requires a terrestrial jammer that is more powerful than the frequencies sent from the satellite.

## Related Attack Patterns
- ChildOf: CAPEC-195

## Resources Required
- A terrestrial satellite jammer with a signal more powerful than that of the satellite attempting to communicate with the target. The adversary must know the location of the target satellite dish.

## Consequences
- Scope: Availability; Impact: Other
