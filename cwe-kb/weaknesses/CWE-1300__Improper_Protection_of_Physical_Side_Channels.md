# CWE-1300: Improper Protection of Physical Side Channels

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1300.html  

## Description
The device does not contain sufficient protection mechanisms to prevent physical side channels from exposing sensitive information due to patterns in physically observable phenomena such as variations in power consumption, electromagnetic emissions (EME), or acoustic emissions.

## Extended Description
An adversary could monitor and measure physical phenomena to detect patterns and make inferences, even if it is not possible to extract the information in the digital domain. Physical side channels have been well-studied for decades in the context of breaking implementations of cryptographic algorithms or other attacks against security features. These side channels may be easily observed by an adversary with physical access to the device, or using a tool that is in close proximity. If the adversary can monitor hardware operation and correlate its data processing with power, EME, and acoustic measurements, the adversary might be able to recover of secret keys and data.

## Related Weaknesses
- ChildOf: CWE-203
- ChildOf: CWE-203

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data

## Potential Mitigations
- [Architecture and Design] Apply blinding or masking techniques to implementations of cryptographic algorithms.
- [Implementation] Add shielding or tamper-resistant protections to the device to increase the difficulty of obtaining measurements of the side-channel.

## Detection Methods
- [Manual Analysis] Perform a set of leakage detection tests such as the procedure outlined in the Test Vector Leakage Assessment (TVLA) test requirements for AES [REF-1230]. TVLA is the basis for the ISO standard 17825 [REF-1229]. A separate methodology is provided by [REF-1228]. Note that sole reliance on this method might not yield expected results [REF-1239] [REF-1240].
- [Manual Analysis] Post-silicon, perform full side-channel attacks (penetration testing) covering as many known leakage models as possible against test code.
- [Manual Analysis] Pre-silicon - while the aforementioned TVLA methods can be performed post-silicon, models of device power consumption or other physical emanations can be built from information present at various stages of the hardware design process before fabrication. TVLA or known side-channel attacks can be applied to these simulated traces and countermeasures applied before tape-out. Academic research in this field includes [REF-1231] [REF-1232] [REF-1233].

## Demonstrative Examples (summary)
- Consider a device that checks a passcode to unlock the screen.
- Consider the device vulnerability CVE-2021-3011, which affects certain microcontrollers [REF-1221]. The Google Titan Security Key is used for two-factor authentication using cryptographic algorithms. The device uses an internal secret key for this purpose and exchanges information based on this key for the authentication. If this internal secret key and the encryption algorithm were known to an adversary, the key function could be duplicated, allowing the adversary to masquerade as the legitimate user.
- The code snippet provided here is part of the modular exponentiation module found in the HACK@DAC'21 Openpiton System-on-Chip (SoC), specifically within the RSA peripheral [REF-1368]. Modular exponentiation, denoted as "a^b mod n," is a crucial operation in the RSA public/private key encryption. In RSA encryption, where 'c' represents ciphertext, 'm' stands for a message, and 'd' corresponds to the private key, the decryption process is carried out using this modular exponentiation as follows: m = c^d mod n, where 'n' is the result of multiplying two large prime numbers.
