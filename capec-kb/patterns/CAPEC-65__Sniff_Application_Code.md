# CAPEC-65: Sniff Application Code

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/65.html  

## Description
An adversary passively sniffs network communications and captures application code bound for an authorized client. Once obtained, they can use it as-is, or through reverse-engineering glean sensitive information or exploit the trust relationship between the client and server. Such code may belong to a dynamic update to the client, a patch being applied to a client component or any such interaction where the client is authorized to communicate with the server.

## Related Attack Patterns
- ChildOf: CAPEC-157
- CanPrecede: CAPEC-37

## Prerequisites
- The attacker must have the ability to place themself in the communication path between the client and server.
- The targeted application must receive some application code from the server; for example, dynamic updates, patches, applets or scripts.
- The attacker must be able to employ a sniffer on the network without being detected.

## Skills Required
- [Medium] The attacker needs to setup a sniffer for a sufficient period of time so as to capture meaningful quantities of code. The presence of the sniffer should not be detected on the network. Also if the attacker plans to employ an adversary-in-the-middle attack (CAPEC-94), the client or server must not realize this. Finally, the attacker needs to regenerate source code from binary code if the need be.

## Resources Required
- The Attacker needs the ability to capture communications between the client being updated and the server providing the update. In the case that encryption obscures client/server communication the attacker will either need to lift key material from the client.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Encrypt all communication between the client and server.
- Implementation: Use SSL, SSH, SCP.
- Operation: Use "ifconfig/ipconfig" or other tools to detect the sniffer installed in the network.

## Related Weaknesses (CWE)
- CWE-319
- CWE-311
- CWE-318
- CWE-693
