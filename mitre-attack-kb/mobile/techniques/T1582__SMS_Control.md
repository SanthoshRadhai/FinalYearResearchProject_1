# T1582: SMS Control


**ATT&CK ID:** T1582  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1582  

## Description
Adversaries may delete, alter, or send SMS messages without user authorization. This could be used to hide C2 SMS messages, spread malware, or various external effects.

This can be accomplished by requesting the `RECEIVE_SMS` or `SEND_SMS` permissions depending on what the malware is attempting to do. If the app is set as the default SMS handler on the device, the `SMS_DELIVER` broadcast intent can be registered, which allows the app to write to the SMS content provider. The content provider directly modifies the messaging database on the device, which could allow malicious applications with this ability to insert, modify, or delete arbitrary messages on the device.(Citation: SMS KitKat)(Citation: Android SmsProvider)

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1095: AhRat
- S0292: AndroRAT
- S0422: Anubis
- S0540: Asacub
- S0655: BusyGasper
- S0480: Cerberus
- S0425: Corona Updates
- S9004: Crocodilus
- S0301: Dendroid
- S0505: Desert Scorpion
- S1054: Drinik
- S1092: Escobar
- S0522: Exobot
- S0509: FakeSpy
- S1067: FluBot
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0551: GoldenEagle
- S1185: LightSpy
- S0485: Mandrake
- S0539: Red Alert 2.0
- S0411: Rotexy
- S1062: S.O.V.A.
- S1055: SharkBot
- S0549: SilkBean
- S1195: SpyC23
- S0328: Stealth Mango
- S0545: TERRACOTTA
- S1069: TangleBot
- S0558: Tiktok Pro
- S0427: TrickMo
- S0489: WolfRAT
