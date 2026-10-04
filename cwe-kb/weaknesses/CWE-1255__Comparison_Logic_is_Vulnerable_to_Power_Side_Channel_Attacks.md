# CWE-1255: Comparison Logic is Vulnerable to Power Side-Channel Attacks

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1255.html  

## Description
A device's real time power consumption may be monitored during security token evaluation and the information gleaned may be used to determine the value of the reference token.

## Extended Description
The power consumed by a device may be instrumented and monitored in real time. If the algorithm for evaluating security tokens is not sufficiently robust, the power consumption may vary by token entry comparison against the reference value. Further, if retries are unlimited, the power difference between a "good" entry and a "bad" entry may be observed and used to determine whether each entry itself is correct thereby allowing unauthorized parties to calculate the reference value.

## Related Weaknesses
- ChildOf: CWE-1300
- PeerOf: CWE-1259

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control, Accountability, Authentication, Authorization, Non-Repudiation; Impact: Modify Memory, Read Memory, Read Files or Directories, Modify Files or Directories, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data, Hide Activities — As compromising a security token may result in complete system control, the impacts are relatively universal.

## Potential Mitigations
- [Architecture and Design] The design phase must consider each check of a security token against a standard and the amount of power consumed during the check of a good token versus a bad token. The alternative is an all at once check where a retry counter is incremented PRIOR to the check.
- [Architecture and Design] Another potential mitigation is to parallelize shifting of secret data (see example 2 below). Note that the wider the bus the more effective the result.
- [Architecture and Design] An additional potential mitigation is to add random data to each crypto operation then subtract it out afterwards. This is highly effective but costly in performance, area, and power consumption. It also requires a random number generator.
- [Implementation] If the architecture is unable to prevent the attack, using filtering components may reduce the ability to implement an attack, however, consideration must be given to the physical removal of the filter elements.
- [Integration] During integration, avoid use of a single secret for an extended period (e.g. frequent key updates). This limits the amount of data compromised but at the cost of complexity of use.

## Demonstrative Examples (summary)
- Consider an example hardware module that checks a user-provided password (or PIN) to grant access to a user. The user-provided password is compared against a stored value byte-by-byte.
- This code demonstrates the transfer of a secret key using Serial-In/Serial-Out shift. It's easy to extract the secret using simple power analysis as each shift gives data on a single bit of the key.
