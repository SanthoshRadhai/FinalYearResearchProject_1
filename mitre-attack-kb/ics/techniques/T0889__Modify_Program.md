# T0889: Modify Program


**ATT&CK ID:** T0889  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0889  

## Description
Adversaries may modify or add a program on a controller to affect how it interacts with the physical process, peripheral devices and other hosts on the network. Modification to controller programs can be accomplished using a Program Download in addition to other types of program modification such as online edit and program append. 

Program modification encompasses the addition and modification of instructions and logic contained in Program Organization Units (POU)  (Citation: IEC February 2013) and similar programming elements found on controllers. This can include, for example, adding new functions to a controller, modifying the logic in existing functions and making new calls from one function to another. 

Some programs may allow an adversary to interact directly with the native API of the controller to take advantage of obscure features or vulnerabilities.

## Mitigations
- M0800: Authorization Enforcement
- M0804: Human User Authentication
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet
