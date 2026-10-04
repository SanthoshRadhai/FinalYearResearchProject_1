# CWE-1302: Missing Source Identifier in Entity Transactions on a System-On-Chip (SOC)

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1302.html  

## Description
The product implements a security identifier mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. A transaction is sent without a security identifier.

## Extended Description
In a System-On-Chip (SoC), various integrated circuits and hardware engines generate transactions such as to access (reads/writes) assets or perform certain actions (e.g., reset, fetch, compute). A typical transaction is comprised of source identity (to identify the originator of the transaction) and a destination identity (to route the transaction to the respective entity) in addition to much more information in the message. Sometimes the transactions are qualified with a Security Identifier. This Security Identifier helps the destination agent decide on the set of allowed or disallowed actions. A weakness that can exist in such transaction schemes is that the source agent does not consistently include the necessary Security Identifier with the transaction. If the Security Identifier is missing, the destination agent might drop the message (resulting in an inadvertent Denial-of-Service (DoS)) or take inappropriate action by default in its attempt to execute the transaction, resulting in privilege escalation or provision of unintended access.

## Related Weaknesses
- ChildOf: CWE-1294

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, DoS: Crash, Exit, or Restart, Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design] Transaction details must be reviewed for design inconsistency and common weaknesses.
- [Implementation] Security identifier definition and programming flow must be tested in pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- Consider a system with a register for storing AES key for encryption or decryption. The key is of 128 bits implemented as a set of four 32-bit registers. The key registers are assets, and the register AES_KEY_ACCESS_POLICY is defined to provide the necessary access controls. The access-policy register defines which agents with a security identifier in the transaction can access the AES-key registers. Each bit in this 32-bit register defines a security identifier. There could be a maximum of 32 security identifiers that are allowed accesses to the AES-key registers. The number of the bit when set (i.e., "1") allows for a respective action from an agent whose identity matches the number of the bit; if set to "0" (i.e., Clear), it disallows the respective action to that corresponding agent.
