# S1104: SLOWPULSE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1104  
**Aliases:** SLOWPULSE  
**Platforms:** Network Devices  

## Description
[SLOWPULSE](https://attack.mitre.org/software/S1104) is a malware that was used by [APT5](https://attack.mitre.org/groups/G1023) as early as 2020 including against U.S. Defense Industrial Base (DIB) companies. [SLOWPULSE](https://attack.mitre.org/software/S1104) has several variants and can modify legitimate Pulse Secure VPN files in order to log credentials and bypass single and two-factor authentication flows.(Citation: Mandiant Pulse Secure Zero-Day April 2021)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1074.001: Local Data Staging
- T1111: Multi-Factor Authentication Interception
- T1554: Compromise Host Software Binary
- T1556.004: Network Device Authentication
- T1556.006: Multi-Factor Authentication
