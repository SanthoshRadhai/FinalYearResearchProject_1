# T0822: External Remote Services


**ATT&CK ID:** T0822  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0822  

## Description
Adversaries may leverage external remote services as a point of initial access into your network. These services allow users to connect to internal network resources from external locations. Examples are VPNs, Citrix, and other access mechanisms. Remote service gateways often manage connections and credential authentication for these services. (Citation: Daniel Oakley, Travis Smith, Tripwire)

External remote services allow administration of a control system from outside the system. Often, vendors and internal engineering groups have access to external remote services to control system networks via the corporate network. In some cases, this access is enabled directly from the internet. While remote access enables ease of maintenance when a control system is in a remote area, compromise of remote access solutions is a liability. The adversary may use these services to gain access to and execute attacks against a control system network. Access to valid accounts is often a requirement. 

As they look for an entry point into the control system network, adversaries may begin searching for existing point-to-point VPN implementations at trusted third party networks or through remote support employee connections where split tunneling is enabled. (Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

## Mitigations
- M0918: User Account Management
- M0927: Password Policies
- M0930: Network Segmentation
- M0932: Multi-factor Authentication
- M0935: Limit Access to Resource Over Network
- M0936: Account Use Policies
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S1157: Fuxnet
