# CAPEC-219: XML Routing Detour Attacks

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/219.html  

## Description
An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of the content. XML Routing Detour Attacks are Adversary in the Middle type attacks (CAPEC-94). The attacker compromises or inserts an intermediate system in the processing of the XML message. For example, WS-Routing can be used to specify a series of nodes or intermediaries through which content is passed. If any of the intermediate nodes in this route are compromised by an attacker they could be used for a routing detour attack. From the compromised system the attacker is able to route the XML process to other nodes of their choice and modify the responses so that the normal chain of processing is unaware of the interception. This system can forward the message to an outside entity and hide the forwarding and processing from the legitimate processing systems by altering the header information.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The targeted system must have multiple stages processing of XML content.

## Skills Required
- [Low] To inject a bogus node in the XML routing table

## Resources Required
- The attacker must be able to insert or compromise a system into the processing path for the transaction.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: Specify maximum number intermediate nodes for the request and require SSL connections with mutual authentication.
- Implementation: Use SSL for connections between all parties with mutual authentication.

## Related Weaknesses (CWE)
- CWE-441
- CWE-610
