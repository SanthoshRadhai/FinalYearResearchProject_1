# T1104: Multi-Stage Channels


**ATT&CK ID:** T1104  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** Linux, macOS, Windows, ESXi  
**Reference:** https://attack.mitre.org/techniques/T1104  

## Description
Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [Fallback Channels](https://attack.mitre.org/techniques/T1008) in case the original first-stage communication path is discovered and blocked.

## Mitigations
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0022: APT3
- G0096: APT41
- G0032: Lazarus Group
- G0069: MuddyWater

## Known Software Using This Technique
- S0031: BACKSPACE
- S0069: BLACKCOFFEE
- S0534: Bazar
- S0220: Chaos
- S1206: JumbledPath
- S1160: Latrodectus
- S1141: LunarWeb
- S1086: Snip3
- S0022: Uroburos
- S0476: Valak
