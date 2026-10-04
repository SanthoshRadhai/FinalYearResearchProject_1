# CWE-1204: Generation of Weak Initialization Vector (IV)

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1204.html  

## Description
The product uses a cryptographic primitive that uses an Initialization Vector (IV), but the product does not generate IVs that are sufficiently unpredictable or unique according to the expected cryptographic requirements for that primitive.

## Extended Description
By design, some cryptographic primitives (such as block ciphers) require that IVs must have certain properties for the uniqueness and/or unpredictability of an IV. Primitives may vary in how important these properties are. If these properties are not maintained, e.g. by a bug in the code, then the cryptography may be weakened or broken by attacking the IVs themselves.

## Related Weaknesses
- ChildOf: CWE-330

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — If the IV is not properly initialized, data that is encrypted can be compromised and information about the data can be leaked. See [REF-1179].

## Potential Mitigations
- [Implementation] Different cipher modes have different requirements for their IVs. When choosing and implementing a mode, it is important to understand those requirements in order to keep security guarantees intact. Generally, it is safest to generate a random IV, since it will be both unpredictable and have a very low chance of being non-unique. IVs do not have to be kept secret, so if generating duplicate IVs is a concern, a list of already-used IVs can be kept and checked against. NIST offers recommendations on generation of IVs for modes of which they have approved. These include options for when random IVs are not practical. For CBC, CFB, and OFB, see [REF-1175]; for GCM, see [REF-1178].

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following examples, CBC mode is used when encrypting data:
- The Wired Equivalent Privacy (WEP) protocol used in the 802.11 wireless standard only supported 40-bit keys, and the IVs were only 24 bits, increasing the chances that the same IV would be reused for multiple messages. The IV was included in plaintext as part of the packet, making it directly observable to attackers. Only 5000 messages are needed before a collision occurs due to the "birthday paradox" [REF-1176]. Some implementations would reuse the same IV for each packet. This IV reuse made it much easier for attackers to recover plaintext from two packets with the same IV, using well-understood attacks, especially if the plaintext was known for one of the packets [REF-1175].
