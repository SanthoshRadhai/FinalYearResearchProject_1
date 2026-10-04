# T0807: Command-Line Interface


**ATT&CK ID:** T0807  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0807  

## Description
Adversaries may utilize command-line interfaces (CLIs) to interact with systems and execute commands. CLIs provide a means of interacting with computer systems and are a common feature across many types of platforms and devices within control systems environments. (Citation: Enterprise ATT&CK January 2018) Adversaries may also use CLIs to install and run new software, including malicious tools that may be installed over the course of an operation.

CLIs are typically accessed locally, but can also be exposed via services, such as SSH, Telnet, and RDP.  Commands that are executed in the CLI execute with the current permissions level of the process running the terminal emulator, unless the command specifies a change in permissions context. Many controllers have CLI interfaces for management purposes.

## Mitigations
- M0938: Execution Prevention
- M0942: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1165: FrostyGoop
- S0604: Industroyer
- S0603: Stuxnet
