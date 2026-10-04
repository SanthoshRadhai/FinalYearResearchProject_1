# CWE-1268: Policy Privileges are not Assigned Consistently Between Control and Data Agents

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1268.html  

## Description
The product's hardware-enforced access control for a particular resource improperly accounts for privilege discrepancies between control and write policies.

## Extended Description
Integrated circuits and hardware engines may provide access to resources (device-configuration, encryption keys, etc.) belonging to trusted firmware or software modules (commonly set by a BIOS or a bootloader). These accesses are typically controlled and limited by the hardware. Hardware design access control is sometimes implemented using a policy. A policy defines which entity or agent may or may not be allowed to perform an action. When a system implements multiple levels of policies, a control policy may allow direct access to a resource as well as changes to the policies themselves. Resources that include agents in their control policy but not in their write policy could unintentionally allow an untrusted agent to insert itself in the write policy register. Inclusion in the write policy register could allow a malicious or misbehaving agent write access to resources. This action could result in security compromises including leaked information, leaked encryption keys, or modification of device configuration.

## Related Weaknesses
- ChildOf: CWE-266

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Files or Directories, Reduce Reliability

## Potential Mitigations
- [Architecture and Design, Implementation] Access-control-policy definition and programming flow must be sufficiently tested in pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- Consider a system of seven registers for storing and configuring an AES key for encryption or decryption. Four 32-bit registers are used to store a 128-bit AES key. The names of those registers are AES_ENC_DEC_KEY_0, AES_ENC_DEC_KEY_1, AES_ENC_DEC_KEY_2, and AES_ENC_DEC_KEY_3. Collectively these are referred to as the AES Key registers. RegisterField description AES_ENC_DEC_KEY_0AES key [0:31] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_1AES key [32:63] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_2AES key [64:95] for encryption or decryptionDefault 0x00000000 AES_ENC_DEC_KEY_3AES key [96:127] for encryption or decryptionDefault 0x00000000 Three 32-bit registers are used to define access control for the AES-key registers. The names of those registers are AES_KEY_CONTROL_POLICY, AES_KEY_READ_POLICY, and AES_KEY_WRITE_POLICY. Collectively these registers are referred to as the Policy registers, and their functions are explained next. The AES_KEY_CONTROL_POLICY register defines which agents can write to the AES_KEY_READ_POLICY or AES_KEY_WRITE_POLICY registers. The AES_KEY_READ_POLICY register defines which agents can read the AES-key registers. The AES_KEY_WRITE_POLICY register defines which agents can write the AES key registers. The preceding three policy registers encode access control at the bit level. Therefore a maximum of 32 agents can be defined (1 bit per agent). The value of the bit when set (i.e., "1") allows the respective action from an agent whose identity corresponds to the number of the bit. If clear (i.e., "0"), it disallows the respective action to that corresponding agent. For example, if bit 0 is set to "1" in the AES_KEY_READ_POLICY register, then agent 0 has permission to read the AES-key registers. Consider that there are 4 agents named Agent 1, Agent 2, Agent 3, and Agent 4. For access control purposes Agent 1 is assigned to bit 1, Agent 2 to bit 2, Agent 3 to bit 3, and Agent 4 to bit 4. All agents are trusted except for Agent 3 who is untrusted. Also consider the register values in the below table.
