# CAPEC-604: Wi-Fi Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/604.html  

## Description
In this attack scenario, the attacker actively transmits on the Wi-Fi channel to prevent users from transmitting or receiving data from the targeted Wi-Fi network. There are several known techniques to perform this attack – for example: the attacker may flood the Wi-Fi access point (e.g. the retransmission device) with deauthentication frames. Another method is to transmit high levels of noise on the RF band used by the Wi-Fi network.

## Related Attack Patterns
- ChildOf: CAPEC-601

## Prerequisites
- Lack of anti-jam features in 802.11
- Lack of authentication on deauthentication/disassociation packets on 802.11-based networks

## Skills Required
- [Low] This attack can be performed by low capability attackers with freely available tools. Commercial tools are also available that can target select networks or all WiFi networks within a range of several miles.

## Consequences
- Scope: Availability; Impact: Other
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Countermeasures have been proposed for both disassociation flooding and RF jamming, however these countermeasures are not standardized and would need to be supported on both the retransmission device and the handset in order to be effective. Commercial products are not currently available that support jamming countermeasures for Wi-Fi.
