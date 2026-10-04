# T0888: Remote System Information Discovery


**ATT&CK ID:** T0888  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0888  

## Description
An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/model, role, and configuration. Adversaries may use information from Remote System Information Discovery to aid in targeting and shaping follow-on behaviors. For example, the system's operational role and model information can dictate whether it is a relevant target for the adversary's operational objectives. In addition, the system's configuration may be used to scope subsequent technique usage. 

Requests for system information are typically implemented using automation and management protocols and are often automatically requested by vendor software during normal operation. This information may be used to tailor management actions, such as program download and system or module firmware. An adversary may leverage this same information by issuing calls directly to the system's API.

## Mitigations
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER
- S0604: Industroyer
- S1072: Industroyer2
- S0603: Stuxnet
