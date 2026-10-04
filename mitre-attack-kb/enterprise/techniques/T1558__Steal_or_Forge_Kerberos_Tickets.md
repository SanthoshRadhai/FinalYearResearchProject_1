# T1558: Steal or Forge Kerberos Tickets


**ATT&CK ID:** T1558  
**Domain:** Mitre Attack  
**Tactic(s):** Credential Access  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1558  

## Description
Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in <code>klist</code> utility can be used to list and analyze cached Kerberos tickets.(Citation: Microsoft Klist)

## Sub-techniques
- T1558.001: Golden Ticket
- T1558.002: Silver Ticket
- T1558.003: Kerberoasting
- T1558.004: AS-REP Roasting
- T1558.005: Ccache Files

## Mitigations
- M1015: Active Directory Configuration
- M1026: Privileged Account Management
- M1027: Password Policies
- M1041: Encrypt Sensitive Information
- M1043: Credential Access Protection
- M1047: Audit

## Known Threat Groups Using This Technique
- G1024: Akira
