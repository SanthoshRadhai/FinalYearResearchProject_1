# T1517: Access Notifications


**ATT&CK ID:** T1517  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1517  

## Description
Adversaries may collect data within notifications sent by the operating system or other applications. Notifications may contain sensitive data such as one-time authentication codes sent over SMS, email, or other mediums. In the case of Credential Access, adversaries may attempt to intercept one-time code sent to the device. Adversaries can also dismiss notifications to prevent the user from noticing that the notification has arrived and can trigger action buttons contained within notifications.(Citation: ESET 2FA Bypass)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy
- M1013: Application Developer Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S0432: Bread
- S1083: Chameleon
- S0425: Corona Updates
- S1092: Escobar
- S1103: FlixOnline
- S1067: FluBot
- S1077: Hornbill
- S0485: Mandrake
- S1062: S.O.V.A.
- S1055: SharkBot
- S1195: SpyC23
- S9006: VajraSpy
- S0489: WolfRAT
