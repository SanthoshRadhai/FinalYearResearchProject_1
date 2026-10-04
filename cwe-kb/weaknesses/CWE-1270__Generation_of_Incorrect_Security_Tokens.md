# CWE-1270: Generation of Incorrect Security Tokens

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1270.html  

## Description
The product implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens generated in the system are incorrect.

## Extended Description
Systems-On-a-Chip (SoC) (Integrated circuits and hardware engines) implement Security Tokens to differentiate and identify actions originated from various agents. These actions could be "read", "write", "program", "reset", "fetch", "compute", etc. Security Tokens are generated and assigned to every agent on the SoC that is either capable of generating an action or receiving an action from another agent. Every agent could be assigned a unique, Security Token based on its trust level or privileges.

## Related Weaknesses
- ChildOf: CWE-284
- ChildOf: CWE-1294

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Files or Directories, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Memory, Modify Memory, DoS: Crash, Exit, or Restart — Incorrectly generated Security Tokens could result in the same token used for multiple agents or multiple tokens being used for the same agent. This condition could result in a Denial-of-Service (DoS) or the execution of an action that in turn could result in privilege escalation or unintended access.

## Potential Mitigations
- [Architecture and Design, Implementation] Generation of Security Tokens should be reviewed for design inconsistency and common weaknesses. Security-Token definition and programming flow should be tested in pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- Consider a system with a register for storing an AES key for encryption or decryption. The key is 128 bits long implemented as a set of four 32-bit registers. The key registers are assets, and register, AES_KEY_ACCESS_POLICY, is defined to provide necessary access controls. The access-policy register defines which agents, using a Security Token, may access the AES-key registers. Each bit in this 32-bit register is used to define a Security Token. There could be a maximum of 32 Security Tokens that are allowed access to the AES-key registers. When set (bit = "1") bit number allows action from an agent whose identity matches that bit number. If Clear (bit = "0") the action is disallowed for the corresponding agent.
