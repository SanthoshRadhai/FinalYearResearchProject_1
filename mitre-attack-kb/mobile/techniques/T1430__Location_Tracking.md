# T1430: Location Tracking


**ATT&CK ID:** T1430  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1430  

## Description
Adversaries may track a device’s physical location through use of standard operating system APIs via malicious or exploited applications on the compromised device. 

 

On Android, applications holding the `ACCESS_COAURSE_LOCATION` or `ACCESS_FINE_LOCATION` permissions provide access to the device’s physical location. On Android 10 and up, declaration of the `ACCESS_BACKGROUND_LOCATION` permission in an application’s manifest will allow applications to request location access even when the application is running in the background.(Citation: Android Request Location Permissions) Some adversaries have utilized integration of Baidu map services to retrieve geographical location once the location access permissions had been obtained.(Citation: PaloAlto-SpyDealer)(Citation: Palo Alto HenBox) 

 

On iOS, applications must include the `NSLocationWhenInUseUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription`, and/or `NSLocationAlwaysUsageDescription` keys in their `Info.plist` file depending on the extent of requested access to location information.(Citation: Apple Requesting Authorization for Location Services) On iOS 8.0 and up, applications call `requestWhenInUseAuthorization()` to request access to location information when the application is in use or `requestAlwaysAuthorization()` to request access to location information regardless of whether the application is in use. With elevated privileges, an adversary may be able to access location data without explicit user consent with the `com.apple.locationd.preauthorized` entitlement key.(Citation: Google Project Zero Insomnia)

## Sub-techniques
- T1430.001: Remote Device Management Services
- T1430.002: Impersonate SS7 Nodes

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy
- M1014: Interconnection Filtering

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0309: Adups
- S1095: AhRat
- S0292: AndroRAT
- S0304: Android/Chuli.A
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S0323: Charger
- S0425: Corona Updates
- S1243: DCHSpy
- S0505: Desert Scorpion
- S9005: DocSwap
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0182: FinFisher
- S0408: FlexiSpy
- S1093: FlyTrap
- S0577: FrozenCell
- S0536: GPlayed
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0291: PJApps
- S0399: Pallas
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S1241: RatMilad
- S0549: SilkBean
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S1216: TriangleDB
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0314: X-Agent for Android
- S0507: eSurv
