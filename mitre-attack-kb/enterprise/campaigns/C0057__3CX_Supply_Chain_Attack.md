# C0057: 3CX Supply Chain Attack

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0057  
**Aliases:** 3CX Supply Chain Attack  

## Description
The [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057) was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with [AppleJeus](https://attack.mitre.org/groups/G1049), access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers.(Citation: Mandiant 3cx UNC4736 2023) While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence.(Citation: Kaspersky 3CX Gopuram 2023) The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.(Citation: 3cx official statement 2023)(Citation: Krebs 3cx overview 2023)
