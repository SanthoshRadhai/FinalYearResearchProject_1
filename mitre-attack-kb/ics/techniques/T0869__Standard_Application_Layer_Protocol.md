# T0869: Standard Application Layer Protocol


**ATT&CK ID:** T0869  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0869  

## Description
Adversaries may establish command and control capabilities over commonly used application layer protocols such as HTTP(S), OPC, RDP, telnet, DNP3, and modbus. These protocols may be used to disguise adversary actions as benign network traffic. Standard protocols may be seen on their associated port or in some cases over a non-standard port.  Adversaries may use these protocols to reach out of the network for command and control, or in some cases to other infected devices within the network.

## Mitigations
- M0807: Network Allowlists
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0049: OilRig

## Known Software Using This Technique
- S0089: BlackEnergy
- S1165: FrostyGoop
- S1045: INCONTROLLER
- S0496: REvil
- S0603: Stuxnet
- S1009: Triton
