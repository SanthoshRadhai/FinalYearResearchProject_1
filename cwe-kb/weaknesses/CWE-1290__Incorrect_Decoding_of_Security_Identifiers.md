# CWE-1290: Incorrect Decoding of Security Identifiers

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1290.html  

## Description
The product implements a decoding mechanism to decode certain bus-transaction signals to security identifiers. If the decoding is implemented incorrectly, then untrusted agents can now gain unauthorized access to the asset.

## Extended Description
In a System-On-Chip (SoC), various integrated circuits and hardware engines generate transactions such as to access (reads/writes) assets or perform certain actions (e.g., reset, fetch, compute, etc.). Among various types of message information, a typical transaction is comprised of source identity (to identify the originator of the transaction) and a destination identity (to route the transaction to the respective entity). Sometimes the transactions are qualified with a security identifier. The security identifier helps the destination agent decide on the set of allowed actions (e.g., access an asset for read and writes). A decoder decodes the bus transactions to map security identifiers into necessary access-controls/protections. A common weakness that can exist in this scenario is incorrect decoding because an untrusted agent's security identifier is decoded into a trusted agent's security identifier. Thus, an untrusted agent previously without access to an asset can now gain access to the asset.

## Related Weaknesses
- ChildOf: CWE-284
- ChildOf: CWE-1294

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Quality Degradation

## Potential Mitigations
- [Architecture and Design] Security identifier decoders must be reviewed for design consistency and common weaknesses.
- [Implementation] Access and programming flows must be tested in pre-silicon and post-silicon testing in order to check for this weakness.

## Demonstrative Examples (summary)
- Consider a system that has four bus masters and a decoder. The decoder is supposed to decode every bus transaction and assign a corresponding security identifier. The security identifier is used to determine accesses to the assets. The bus transaction that contains the security information is Bus_transaction [15:14], and the bits 15 through 14 contain the security identifier information. The table below provides bus masters as well as their security identifiers and trust assumptions: Bus MasterSecurity Identifier DecodingTrust Assumptions Master_0"00"Untrusted Master_1"01"Trusted Master_2"10"Untrusted Master_3"11"Untrusted The assets are the AES-Key registers for encryption or decryption. The key is 128 bits implemented as a set of four 32-bit registers. The AES_KEY_ACCESS_POLICY is used to define which agents with a security identifier in the transaction can access the AES-key registers. The size of the security identifier is 4 bits (i.e., bit 3 through 0). Each bit in these 4 bits defines a security identifier. There are only 4 security identifiers that are allowed accesses to the AES-key registers. The number of the bit when set (i.e., "1") allows respective action from an agent whose identity matches the number of the bit. If clear (i.e., "0"), disallows the respective action to that corresponding agent. RegisterField description AES_ENC_DEC_KEY_0AES key [0:31] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_1AES key [32:63] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_2AES key [64:95] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_3AES key [96:127] for encryption or decryptionDefault 0x00000000 AES_KEY_ACCESS_POLCY[31:4] Default 0x00000000[3:0]-0x01 agent with Security Identified "1" has access to AES_ENC_DEC_KEY_0 through AES_ENC_DEC_KEY_3 registers
