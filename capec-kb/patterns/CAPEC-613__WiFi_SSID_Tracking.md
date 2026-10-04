# CAPEC-613: WiFi SSID Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/613.html  

## Description
In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients that are accessing the network (e.g., the handset/mobile device). Once the attacker is able to associate an SSID with a particular user or set of users (for example, when attending a public event), the attacker can then scan for this SSID to track that user in the future.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- None

## Skills Required
- [Low] Open source and commercial software tools are available and open databases of known WiFi SSID addresses are available online.

## Mitigations
- Do not enable the feature of "Hidden SSIDs" (also known as "Network Cloaking") – this option disables the usual broadcasting of the SSID by the access point, but forces the mobile handset to send requests on all supported radio channels which contains the SSID. The result is that tracking of the mobile device becomes easier since it is transmitting the SSID more frequently.
- Frequently change the SSID to new and unrelated values

## Related Weaknesses (CWE)
- CWE-201
- CWE-300
