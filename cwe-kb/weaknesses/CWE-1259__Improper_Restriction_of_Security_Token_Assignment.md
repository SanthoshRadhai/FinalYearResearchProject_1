# CWE-1259: Improper Restriction of Security Token Assignment

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1259.html  

## Description
The System-On-A-Chip (SoC) implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens are improperly protected.

## Extended Description
Systems-On-A-Chip (Integrated circuits and hardware engines) implement Security Tokens to differentiate and identify which actions originated from which agent. These actions may be one of the directives: 'read', 'write', 'program', 'reset', 'fetch', 'compute', etc. Security Tokens are assigned to every agent in the System that is capable of generating an action or receiving an action from another agent. Multiple Security Tokens may be assigned to an agent and may be unique based on the agent's trust level or allowed privileges. Since the Security Tokens are integral for the maintenance of security in an SoC, they need to be protected properly. A common weakness afflicting Security Tokens is improperly restricting the assignment to trusted components.

## Related Weaknesses
- ChildOf: CWE-284
- ChildOf: CWE-1294

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Files or Directories, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Modify Memory, Modify Memory, DoS: Crash, Exit, or Restart — An improperly protected Security Token may be able to be programmed by a malicious agent (i.e., the Security Token is mutable) to spoof the action as if it originated from a trusted agent.

## Potential Mitigations
- [Architecture and Design, Implementation] Security Token assignment review checks for design inconsistency and common weaknesses. Security-Token definition and programming flow is tested in both pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- For example, consider a system with a register for storing an AES key for encryption and decryption. The key is of 128 bits implemented as a set of four 32-bit registers. The key register assets have an associated control register, AES_KEY_ACCESS_POLICY, which provides the necessary access controls. This access-policy register defines which agents may engage in a transaction, and the type of transaction, with the AES-key registers. Each bit in this 32-bit register defines a security Token. There could be a maximum of 32 security Tokens that are allowed access to the AES-key registers. The number of the bit when set (i.e., "1") allows respective action from an agent whose identity matches the number of the bit and, if "0" (i.e., Clear), disallows the respective action to that corresponding agent.
