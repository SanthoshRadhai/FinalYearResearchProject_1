# CWE-1241: Use of Predictable Algorithm in Random Number Generator

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1241.html  

## Description
The device uses an algorithm that is predictable and generates a pseudo-random number.

## Extended Description
Pseudo-random number generator algorithms are predictable because their registers have a finite number of possible states, which eventually lead to repeating patterns. As a result, pseudo-random number generators (PRNGs) can compromise their randomness or expose their internal state to various attacks, such as reverse engineering or tampering.

## Related Weaknesses
- ChildOf: CWE-330

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design] It is highly recommended to use a true random number generator (TRNG) to ensure the security of encryption schemes. Hardware-based TRNGs generate unpredictable, unbiased, and independent random numbers because they employ physical phenomena, e.g., electrical noise, as sources to generate random numbers.
- [Implementation] It is highly recommended to use a true random number generator (TRNG) to ensure the security of encryption schemes. Hardware-based TRNGs generate unpredictable, unbiased, and independent random numbers because they employ physical phenomena, e.g., electrical noise, as sources to generate random numbers.

## Demonstrative Examples (summary)
- Suppose a cryptographic function expects random value to be supplied for the crypto algorithm.
- The example code is taken from the PRNG inside the buggy OpenPiton SoC of HACK@DAC'21 [REF-1370]. The SoC implements a pseudo-random number generator using a Linear Feedback Shift Register (LFSR).
