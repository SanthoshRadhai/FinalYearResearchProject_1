# CWE-332: Insufficient Entropy in PRNG

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/332.html  

## Description
The lack of entropy available for, or used by, a Pseudo-Random Number Generator (PRNG) can be a stability and security threat.

## Related Weaknesses
- ChildOf: CWE-331

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — If a pseudo-random number generator is using a limited entropy source which runs out (if the generator fails closed), the program may pause or crash.
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — If a PRNG is using a limited entropy source which runs out, and the generator fails open, the generator could produce predictable random numbers. Potentially a weak source of random numbers could weaken the encryption method used for authentication of users.

## Potential Mitigations
- [Architecture and Design, Requirements] Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").
- [Implementation] Consider a PRNG that re-seeds itself as needed from high-quality pseudo-random output, such as hardware devices.
- [Architecture and Design] When deciding which PRNG to use, look at its sources of entropy. Depending on what your security needs are, you may need to use a random number generator that always uses strong random data -- i.e., a random number generator that attempts to be strong but will fail in a weak way or will always provide some middle ground of protection through techniques like re-seeding. Generally, something that always provides a predictable amount of strength is preferable.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
