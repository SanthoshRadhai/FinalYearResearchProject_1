# CWE-1267: Policy Uses Obsolete Encoding

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1267.html  

## Description
The product uses an obsolete encoding mechanism to implement access controls.

## Extended Description
Within a System-On-a-Chip (SoC), various circuits and hardware engines generate transactions for the purpose of accessing (read/write) assets or performing various actions (e.g., reset, fetch, compute, etc.). Among various types of message information, a typical transaction is comprised of source identity (identifying the originator of the transaction) and a destination identity (routing the transaction to the respective entity). Sometimes the transactions are qualified with a Security Token. This Security Token helps the destination agent decide on the set of allowed actions (e.g., access to an asset for reads and writes). A policy encoder is used to map the bus transactions to Security Tokens that in turn are used as access-controls/protection mechanisms. A common weakness involves using an encoding which is no longer trusted, i.e., an obsolete encoding.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, Modify Files or Directories, Read Files or Directories, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Reduce Reliability

## Potential Mitigations
- [Architecture and Design, Implementation] Security Token Decoders should be reviewed for design inconsistency and common weaknesses. Access and programming flows should be tested in both pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- For example, consider a system that has four bus masters. The table below provides bus masters, their Security Tokens, and trust assumptions. Bus Master Security Token Decoding Trust Assumptions Master_0 "00" Untrusted Master_1 "01" Trusted Master_2 "10" Untrusted Master_3 "11" Untrusted The policy encoding is to be defined such that Security Token will be used in implemented access-controls. The bits in the bus transaction that contain Security-Token information are Bus_transaction [15:11]. The assets are the AES-Key registers for encryption or decryption. The key of 128 bits is implemented as a set of four, 32-bit registers. Register Field description AES_ENC_DEC_KEY_0 AES key [0:31] for encryption or decryption, Default 0x00000000 AES_ENC_DEC_KEY_1 AES key [32:63] for encryption or decryption, Default 0x00000000 AES_ENC_DEC_KEY_2 AES key [64:95] for encryption or decryption, Default 0x00000000 AES_ENC_DEC_KEY_4 AES key [96:127] for encryption or decryption, Default 0x00000000 Below is an example of a policy encoding scheme inherited from a previous project where all "ODD" numbered Security Tokens are trusted.
