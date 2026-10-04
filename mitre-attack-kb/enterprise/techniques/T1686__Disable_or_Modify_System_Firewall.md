# T1686: Disable or Modify System Firewall


**ATT&CK ID:** T1686  
**Domain:** Mitre Attack  
**Tactic(s):** Defense Impairment  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1686  

## Description
Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies, or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles, altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port.(Citation: change_rdp_port_conti)

Adversaries may disable or modify firewalls using different behaviors, depending on the platform. For example, in ESXi, firewall rules may be modified directly via the esxcli (e.g., via esxcli network firewall set) or via the vCenter user interface.(Citation: Broadcom ESXi Firewall)(Citation: Trellix Rnasomhouse 2024)

## Sub-techniques
- T1686.001: Cloud Firewall
- T1686.002: Network Device Firewall
- T1686.003: Windows Host Firewall

## Mitigations
- M1018: User Account Management
- M1022: Restrict File and Directory Permissions
- M1024: Restrict Registry Permissions
- M1047: Audit

## Known Threat Groups Using This Technique
- G0082: APT38
- G1043: BlackByte
- G0008: Carbanak
- G0035: Dragonfly
- G0046: FIN7
- G0094: Kimsuky
- G1051: Medusa Group
- G0106: Rocke
- G1045: Salt Typhoon
- G0139: TeamTNT
- G1022: ToddyCat
- G1048: UNC3886
- G1047: Velvet Ant

## Known Software Using This Technique
- S0031: BACKSPACE
- S1161: BPFDoor
- S0492: CookieMiner
- S0531: Grandoreiro
- S0376: HOPLIGHT
- S1211: Hannotog
- S0260: InvisiMole
- S0088: Kasidet
- S0336: NanoCore
- S0013: PlugX
- S1032: PyDCrypt
- S1178: ShrinkLocker
- S1223: THINCRUST
- S0412: ZxShell
- S0108: netsh
