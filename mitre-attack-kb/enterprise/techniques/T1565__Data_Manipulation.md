# T1565: Data Manipulation


**ATT&CK ID:** T1565  
**Domain:** Mitre Attack  
**Tactic(s):** Impact  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1565  

## Description
Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, thus threatening the integrity of the data.(Citation: Sygnia Elephant Beetle Jan 2022) By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Sub-techniques
- T1565.001: Stored Data Manipulation
- T1565.002: Transmitted Data Manipulation
- T1565.003: Runtime Data Manipulation

## Mitigations
- M1022: Restrict File and Directory Permissions
- M1029: Remote Data Storage
- M1030: Network Segmentation
- M1041: Encrypt Sensitive Information

## Known Threat Groups Using This Technique
- G1016: FIN13

## Known Software Using This Technique
- S9014: PHASEJAM
