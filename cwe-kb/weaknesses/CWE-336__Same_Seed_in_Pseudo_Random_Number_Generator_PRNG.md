# CWE-336: Same Seed in Pseudo-Random Number Generator (PRNG)

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/336.html  

## Description
A Pseudo-Random Number Generator (PRNG) uses the same seed each time the product is initialized.

## Extended Description
Given the deterministic nature of PRNGs, using the same seed for each initialization will lead to the same output in the same order. If an attacker can guess (or knows) the seed, then the attacker may be able to determine the random numbers that will be produced from the PRNG.

## Related Weaknesses
- ChildOf: CWE-335

## Common Consequences
- Scope: Other, Access Control; Impact: Other, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Do not reuse PRNG seeds. Consider a PRNG that periodically re-seeds itself as needed from a high quality pseudo-random output, such as hardware devices.
- [Architecture and Design, Requirements] Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems, or use the more recent FIPS 140-3 [REF-1192] if possible.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code uses a statistical PRNG to generate account IDs.
- This code attempts to generate a unique random identifier for a user's session.
