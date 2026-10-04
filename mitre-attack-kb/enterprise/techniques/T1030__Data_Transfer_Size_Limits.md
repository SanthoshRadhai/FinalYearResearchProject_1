# T1030: Data Transfer Size Limits


**ATT&CK ID:** T1030  
**Domain:** Mitre Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Linux, macOS, Windows, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1030  

## Description
An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Mitigations
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0007: APT28
- G0096: APT41
- G1014: LuminousMoth
- G1040: Play
- G0027: Threat Group-3390

## Known Software Using This Technique
- S0622: AppleSeed
- S0030: Carbanak
- S0154: Cobalt Strike
- S0170: Helminth
- S0487: Kessel
- S1020: Kevin
- S1141: LunarWeb
- S0699: Mythic
- S0644: ObliqueRAT
- S0264: OopsIE
- S0150: POSHSPY
- S0495: RDAT
- S1040: Rclone
- S1200: StealBit
