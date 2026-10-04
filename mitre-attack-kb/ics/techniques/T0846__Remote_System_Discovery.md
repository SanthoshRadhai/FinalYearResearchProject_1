# T0846: Remote System Discovery


**ATT&CK ID:** T0846  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0846  

## Description
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for subsequent Lateral Movement or Discovery techniques. Functionality could exist within adversary tools to enable this, but utilities available on the operating system or vendor software could also be used.(Citation: Enterprise ATT&CK January 2018)

## Sub-techniques
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery

## Mitigations
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER
- S0604: Industroyer
