# T1480: Execution Guardrails


**ATT&CK ID:** T1480  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1480  

## Description
Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.(Citation: FireEye Kevin Mandia Guardrails) Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.(Citation: FireEye Outlook Dec 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497). While use of [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.(Citation: Trellix-Qakbot)

## Sub-techniques
- T1480.001: Environmental Keying
- T1480.002: Mutual Exclusion

## Mitigations
- M1055: Do Not Mitigate

## Known Threat Groups Using This Technique
- G0099: APT-C-36
- G1043: BlackByte
- G1052: Contagious Interview
- G0047: Gamaredon Group

## Known Software Using This Technique
- S1194: Akira _v2
- S0504: Anchor
- S1133: Apostle
- S1184: BOLDMOVE
- S1161: BPFDoor
- S0570: BitPaymer
- S1180: BlackByte Ransomware
- S0635: BoomBox
- S1149: CHIMNEYSWEEP
- S9042: CanisterWorm
- S1052: DEADEYE
- S1111: DarkGate
- S0634: EnvyScout
- S1179: Exbyte
- S9010: GlassWorm
- S9023: HiddenFace
- S9020: LODEINFO
- S9039: LazyWiper
- S1185: LightSpy
- S1199: LockBit 2.0
- S1202: LockBit 3.0
- S1143: LunarLoader
- S9043: Mini Shai-Hulud
- S0637: NativeZone
- S9019: PureCrypter
- S1242: Qilin
- S1150: ROADSWEEP
- S9026: ROAMINGHOUSE
- S1212: RansomHub
- S1130: Raspberry Robin
- S1240: RedLine Stealer
- S0562: SUNSPOT
- S1210: Sagerunex
- S1178: ShrinkLocker
- S1035: Small Sieve
- S1200: StealBit
- S1183: StrelaStealer
- S0603: Stuxnet
- S9001: SystemBC
- S1239: TONESHELL
- S9041: TeamPCP Cloud Stealer
- S0678: Torisma
- S9034: Tsundere Botnet
- S0636: VaporRage
- S9003: evilginx2
