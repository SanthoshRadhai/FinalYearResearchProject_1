# CWE-335: Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG)

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/335.html  

## Description
The product uses a Pseudo-Random Number Generator (PRNG) but does not correctly manage seeds.

## Extended Description
PRNGs are deterministic and, while their output appears random, they cannot actually create entropy. They rely on cryptographically secure and unique seeds for entropy so proper seeding is critical to the secure operation of the PRNG. Management of seeds could be broken down into two main areas: (1) protecting seeds as cryptographic material (such as a cryptographic key); (2) whenever possible, using a uniquely generated seed from a cryptographically secure source PRNGs require a seed as input to generate a stream of numbers that are functionally indistinguishable from random numbers. While the output is, in many cases, sufficient for cryptographic uses, the output of any PRNG is directly determined by the seed provided as input. If the seed can be ascertained by a third party, the entire output of the PRNG can be made known to them. As such, the seed should be kept secret and should ideally not be able to be guessed. For example, the current time may be a poor seed. Knowing the approximate time the PRNG was seeded greatly reduces the possible key space. Seeds do not necessarily need to be unique, but reusing seeds may open up attacks if the seed is discovered.

## Related Weaknesses
- ChildOf: CWE-330
- ChildOf: CWE-330

## Common Consequences
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — If a PRNG is used incorrectly, such as using the same seed for each initialization or using a predictable seed, then an attacker may be able to easily guess the seed and thus the random numbers. This could lead to unauthorized access to a system if the seed is used for authentication and authorization.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code uses a statistical PRNG to generate account IDs.
- Both of these examples use a statistical PRNG seeded with the current value of the system clock to generate a random number:
- This code grabs some random bytes and uses them for a seed in a PRNG, in order to generate a new cryptographic key.
