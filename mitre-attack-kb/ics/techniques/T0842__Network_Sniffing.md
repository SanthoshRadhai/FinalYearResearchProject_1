# T0842: Network Sniffing


**ATT&CK ID:** T0842  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0842  

## Description
Network sniffing is the practice of using a network interface on a computer system to monitor or capture information (Citation: Enterprise ATT&CK January 2018) regardless of whether it is the specified destination for the information. 

An adversary may attempt to sniff the traffic to gain information about the target. This information can vary in the level of importance. Relatively unimportant information is general communications to and from machines.  Relatively important information would be login information. User credentials may be sent over an unencrypted protocol, such as Telnet, that can be captured and obtained through network packet analysis. 

In addition, ARP and Domain Name Service (DNS) poisoning can be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

## Mitigations
- M0808: Encrypt Network Traffic
- M0814: Static Network Configuration
- M0926: Privileged Account Management
- M0930: Network Segmentation
- M0932: Multi-factor Authentication

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0603: Stuxnet
- S1010: VPNFilter
