# CAPEC-609: Cellular Traffic Intercept

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/609.html  

## Description
Cellular traffic for voice and data from mobile devices and retransmission devices can be intercepted via numerous methods. Malicious actors can deploy their own cellular tower equipment and intercept cellular traffic surreptitiously. Additionally, government agencies of adversaries and malicious actors can intercept cellular traffic via the telecommunications backbone over which mobile traffic is transmitted.

## Related Attack Patterns
- ChildOf: CAPEC-157

## Prerequisites
- None

## Skills Required
- [Medium] Adversaries can purchase hardware and software solutions, or create their own solutions, to capture/intercept cellular radio traffic. The cost of a basic Base Transceiver Station (BTS) to broadcast to local mobile cellular radios in mobile devices has dropped to very affordable costs. The ability of commercial cellular providers to monitor for "rogue" BTS stations is poor in many areas and it is assumed that "rogue" BTS stations exist in urban areas.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encryption of all data packets emanating from the smartphone to a retransmission device via two encrypted tunnels with Suite B cryptography, all the way to the VPN gateway at the datacenter.

## Related Weaknesses (CWE)
- CWE-311
