# T1027: Obfuscated Files or Information


**ATT&CK ID:** T1027  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Reference:** https://attack.mitre.org/techniques/T1027  

## Description
Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 

Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) for [User Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.(Citation: Volexity PowerDuke November 2016) Adversaries may also use compressed or archived scripts, such as JavaScript. 

Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery.(Citation: Linux/Cdorked.A We Live Security Analysis) Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation: Carbon Black Obfuscation Sept 2016)

Adversaries may also abuse [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010) to obscure commands executed from payloads or directly via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms.(Citation: FireEye Obfuscation June 2017)(Citation: FireEye Revoke-Obfuscation July 2017)(Citation: PaloAlto EncodedCommand March 2017)

## Sub-techniques
- T1027.001: Binary Padding
- T1027.002: Software Packing
- T1027.003: Steganography
- T1027.004: Compile After Delivery
- T1027.005: Indicator Removal from Tools
- T1027.006: HTML Smuggling
- T1027.007: Dynamic API Resolution
- T1027.008: Stripped Payloads
- T1027.009: Embedded Payloads
- T1027.010: Command Obfuscation
- T1027.011: Fileless Storage
- T1027.012: LNK Icon Smuggling
- T1027.013: Encrypted/Encoded File
- T1027.014: Polymorphic Code
- T1027.015: Compression
- T1027.016: Junk Code Insertion
- T1027.017: SVG Smuggling
- T1027.018: Invisible Unicode

## Mitigations
- M1017: User Training
- M1040: Behavior Prevention on Endpoint
- M1047: Audit
- M1049: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G0022: APT3
- G0067: APT37
- G0096: APT41
- G0135: BackdoorDiplomacy
- G0063: BlackOasis
- G1006: Earth Lusca
- G0093: GALLIUM
- G0084: Gallmaker
- G0047: Gamaredon Group
- G0004: Ke3chang
- G0094: Kimsuky
- G1036: Moonstone Sleet
- G0129: Mustang Panda
- G1039: RedCurl
- G0106: Rocke
- G0034: Sandworm Team
- G0112: Windshift

## Known Software Using This Technique
- S0045: ADVSTORESHELL
- S9027: ANELLDR
- S1028: Action RAT
- S0331: Agent Tesla
- S1025: Amadey
- S0504: Anchor
- S0584: AppleJeus
- S0622: AppleSeed
- S0640: Avaddon
- S1053: AvosLocker
- S1226: BOOKWORM
- S1161: BPFDoor
- S9015: BRICKSTORM
- S1118: BUSHWALK
- S0635: BoomBox
- S0651: BoxCaon
- S1063: Brute Ratel C4
- S1039: Bumblebee
- S0482: Bundlore
- S0465: CARROTBALL
- S1149: CHIMNEYSWEEP
- S1105: COATHANGER
- S0137: CORESHELL
- S0030: Carbanak
- S0335: Carbon
- S0660: Clambling
- S0154: Cobalt Strike
- S0369: CoinTicker
- S0126: ComRAT
- S0244: Comnie
- S0608: Conficker
- S0575: Conti
- S0625: Cuba
- S0694: DRATzarus
- S1111: DarkGate
- S1066: DarkTortilla
- S0187: Daserf
- S0354: Denis
- S0659: Diavol
- S0384: Dridex
- S0502: Drovorub
- S0062: DustySky
- S0593: ECCENTRICBANDWAGON
- S0605: EKANS
- S0377: Ebury
- S0624: Ecipekac
- S0091: Epic
- S0512: FatDuke
- S0182: FinFisher
- S0355: Final1stspy
- S0696: Flagpro
- S9033: Fooder
- S1138: Gootloader
- S0690: Green Lambert
- S0632: GrimAgent
- S0132: H1N1
- S0070: HTTPBrowser
- S9007: HTTPTroy
- S0499: Hancitor
- S0203: Hydraq
- S0189: ISMInjector
- S0434: Imminent Monitor
- S0604: Industroyer
- S0259: InnaputRAT
- S0260: InvisiMole
- S0201: JPIN
- S0265: Kazuar
- S0607: KillDisk
- S0641: Kobalos
- S9020: LODEINFO
- S0681: Lizar
- S0447: Lokibot
- S1213: Lumma Stealer
- S0500: MCMD
- S0167: Matryoshka
- S0449: Maze
- S0051: MiniDuke
- S0198: NETWIRE
- S0353: NOKKI
- S9025: NOOPLDR
- S0336: NanoCore
- S1090: NightClub
- S0138: OLDBAIT
- S0264: OopsIE
- S0229: Orz
- S0594: Out1
- S0598: P.A.S. Webshell
- S0150: POSHSPY
- S1228: PUBLOAD
- S0196: PUNCHBUGGY
- S0197: PUNCHTRACK
- S0517: Pillowmint
- S0124: Pisloader
- S0013: PlugX
- S0428: PoetRAT
- S0012: PoisonIvy
- S0518: PolyglotDuke
- S0393: PowerStallion
- S0650: QakBot
- S0240: ROKRAT
- S0148: RTM
- S0458: Ramsay
- S1130: Raspberry Robin
- S0511: RegDuke
- S0332: Remcos
- S9037: RustyWater
- S0446: Ryuk
- S0461: SDBbot
- S0063: SHOTPUT
- S1104: SLOWPULSE
- S0559: SUNBURST
- S0562: SUNSPOT
- S1064: SVCReady
- S1018: Saint Bot
- S1099: Samurai
- S1085: Sardonic
- S0596: ShadowPad
- S9008: Shai-Hulud
- S0140: Shamoon
- S0445: ShimRatReporter
- S0623: Siloscape
- S0633: Sliver
- S1035: Small Sieve
- S1086: Snip3
- S0627: SodaMaster
- S0615: SombRAT
- S0516: SoreFang
- S0142: StreamEx
- S1183: StrelaStealer
- S0242: SynAck
- S0560: TEARDROP
- S0467: TajMahal
- S0266: TrickBot
- S0094: Trojan.Karagany
- S0647: Turian
- S0476: Valak
- S0117: XTunnel
- S0283: jRAT
