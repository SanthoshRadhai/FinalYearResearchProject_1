# T1011: Exfiltration Over Other Network Medium


**ATT&CK ID:** T1011  
**Domain:** Mitre Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1011  

## Description
Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Sub-techniques
- T1011.001: Exfiltration Over Bluetooth

## Mitigations
- M1028: Operating System Configuration
- M1042: Disable or Remove Feature or Program
