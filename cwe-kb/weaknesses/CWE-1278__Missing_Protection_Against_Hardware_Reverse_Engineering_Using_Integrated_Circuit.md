# CWE-1278: Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1278.html  

## Description
Information stored in hardware may be recovered by an attacker with the capability to capture and analyze images of the integrated circuit using techniques such as scanning electron microscopy.

## Extended Description
The physical structure of a device, viewed at high enough magnification, can reveal the information stored inside. Typical steps in IC reverse engineering involve removing the chip packaging (decapsulation) then using various imaging techniques ranging from high resolution x-ray microscopy to invasive techniques involving removing IC layers and imaging each layer using a scanning electron microscope. The goal of such activities is to recover secret keys, unique device identifiers, and proprietary code and circuit designs embedded in hardware that the attacker has been unsuccessful at accessing through other means. These secrets may be stored in non-volatile memory or in the circuit netlist. Memory technologies such as masked ROM allow easier to extraction of secrets than One-time Programmable (OTP) memory.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Confidentiality; Impact: Varies by Context — A common goal of malicious actors who reverse engineer ICs is to produce and sell counterfeit versions of the IC.

## Potential Mitigations
- [Architecture and Design] The cost of secret extraction via IC reverse engineering should outweigh the potential value of the secrets being extracted. Threat model and value of secrets should be used to choose the technology used to safeguard those secrets. Examples include IC camouflaging and obfuscation, tamper-proof packaging, active shielding, and physical tampering detection information erasure.

## Demonstrative Examples (summary)
- Consider an SoC design that embeds a secret key in read-only memory (ROM). The key is baked into the design logic and may not be modified after fabrication causing the key to be identical for all devices. An attacker in possession of the IC can decapsulate and delayer the device. After imaging the layers, computer vision algorithms or manual inspection of the circuit features locate the ROM and reveal the value of the key bits as encoded in the visible circuit structure of the ROM.
