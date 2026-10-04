# CWE-339: Small Seed Space in PRNG

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/339.html  

## Description
A Pseudo-Random Number Generator (PRNG) uses a relatively small seed space, which makes it more susceptible to brute force attacks.

## Extended Description
PRNGs are entirely deterministic once seeded, so it should be extremely difficult to guess the seed. If an attacker can collect the outputs of a PRNG and then brute force the seed by trying every possibility to see which seed matches the observed output, then the attacker will know the output of any subsequent calls to the PRNG. A small seed space implies that the attacker will have far fewer possible values to try to exhaust all possibilities.

## Related Weaknesses
- ChildOf: CWE-335
- PeerOf: CWE-341

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Potential Mitigations
- [Architecture and Design] Use well vetted pseudo-random number generating algorithms with adequate length seeds. Pseudo-random number generators can produce predictable numbers if the generator is known and the seed can be guessed. A 256-bit seed is a good starting point for producing a "random enough" number.
- [Architecture and Design, Requirements] Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems, or use the more recent FIPS 140-3 [REF-1192] if possible.

## Demonstrative Examples (summary)
- This code grabs some random bytes and uses them for a seed in a PRNG, in order to generate a new cryptographic key.
