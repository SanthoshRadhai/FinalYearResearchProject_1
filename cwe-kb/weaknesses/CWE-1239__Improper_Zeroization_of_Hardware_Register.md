# CWE-1239: Improper Zeroization of Hardware Register

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1239.html  

## Description
The hardware product does not properly clear sensitive information from built-in registers when the user of the hardware block changes.

## Extended Description
Hardware logic operates on data stored in registers local to the hardware block. Most hardware IPs, including cryptographic accelerators, rely on registers to buffer I/O, store intermediate values, and interface with software. The result of this is that sensitive information, such as passwords or encryption keys, can exist in locations not transparent to the user of the hardware logic. When a different entity obtains access to the IP due to a change in operating mode or conditions, the new entity can extract information belonging to the previous user if no mechanisms are in place to clear register contents. It is important to clear information stored in the hardware if a physical attack on the product is detected, or if the user of the hardware block changes. The process of clearing register contents in a hardware IP is referred to as zeroization in standards for cryptographic hardware modules such as FIPS-140-2 [REF-267].

## Related Weaknesses
- ChildOf: CWE-226
- ChildOf: CWE-226

## Common Consequences
- Scope: Confidentiality; Impact: Varies by Context — The consequences will depend on the information disclosed due to the vulnerability.

## Potential Mitigations
- [Architecture and Design] Every register potentially containing sensitive information must have a policy specifying how and when information is cleared, in addition to clarifying if it is the responsibility of the hardware logic or IP user to initiate the zeroization procedure at the appropriate time.

## Demonstrative Examples (summary)
- Suppose a hardware IP for implementing an encryption routine works as expected, but it leaves the intermediate results in some registers that can be accessed. Exactly why this access happens is immaterial - it might be unintentional or intentional, where the designer wanted a "quick fix" for something.
- The example code below [REF-1379] is taken from the SHA256 Interface/wrapper controller module of the HACK@DAC'21 buggy OpenPiton SoC. Within the wrapper module there are a set of 16 memory-mapped registers referenced data[0] to data[15]. These registers are 32 bits in size and are used to store the data received on the AXI Lite interface for hashing. Once both the message to be hashed and a request to start the hash computation are received, the values of these registers will be forwarded to the underlying SHA256 module for processing. Once forwarded, the values in these registers no longer need to be retained. In fact, if not cleared or overwritten, these sensitive values can be read over the AXI Lite interface, potentially compromising any previously confidential data stored therein.
