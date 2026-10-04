# CAPEC-157: Sniffing Attacks

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/157.html  

## Description
In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient. Sniffing Attacks are similar to Adversary-In-The-Middle attacks (CAPEC-94), but are entirely passive. AiTM attacks are predominantly active and often alter the content of the communications themselves.

## Related Attack Patterns
- ChildOf: CAPEC-117
- CanPrecede: CAPEC-652

## Prerequisites
- The target data stream must be transmitted on a medium to which the adversary has access.

## Resources Required
- The adversary must be able to intercept the transmissions containing the data of interest. Depending on the medium of transmission and the path the data takes between the sender and recipient, the adversary may require special equipment and/or require that this equipment be placed in specific locations (e.g., a network sniffing tool)

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encrypt sensitive information when transmitted on insecure mediums to prevent interception.

## Related Weaknesses (CWE)
- CWE-311
