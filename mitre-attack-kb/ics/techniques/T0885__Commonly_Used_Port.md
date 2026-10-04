# T0885: Commonly Used Port


**ATT&CK ID:** T0885  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0885  

## Description
Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to blend in with normal network activity, to avoid more detailed inspection. They may use the protocol associated with the port, or a completely different protocol. They may use commonly open ports, such as the examples provided below. 
 
 * TCP:80 (HTTP) 
 * TCP:443 (HTTPS) 
 * TCP/UDP:53 (DNS) 
 * TCP:1024-4999 (OPC on XP/Win2k3) 
 * TCP:49152-65535 (OPC on Vista and later) 
 * TCP:23 (TELNET) 
 * UDP:161 (SNMP) 
 * TCP:502 (MODBUS) 
 * TCP:102 (S7comm/ISO-TSAP) 
 * TCP:20000 (DNP3) 
 * TCP:44818 (Ethernet/IP)

## Mitigations
- M0804: Human User Authentication
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S1165: FrostyGoop
- S0603: Stuxnet
- S1009: Triton
