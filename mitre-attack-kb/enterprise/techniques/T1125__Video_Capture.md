# T1125: Video Capture


**ATT&CK ID:** T1125  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1125  

## Description
An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1113) due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. (Citation: objective-see 2017 review)

## Known Threat Groups Using This Technique
- G1003: Ember Bear
- G0046: FIN7
- G0091: Silence
- G1055: VOID MANTICORE

## Known Software Using This Technique
- S0331: Agent Tesla
- S1087: AsyncRAT
- S0234: Bandook
- S0660: Clambling
- S0338: Cobian RAT
- S0591: ConnectWise
- S0115: Crimson
- S0334: DarkComet
- S0021: Derusbi
- S0363: Empire
- S0152: EvilGrab
- S0434: Imminent Monitor
- S0260: InvisiMole
- S0265: Kazuar
- S0409: Machete
- S0336: NanoCore
- S0644: ObliqueRAT
- S1050: PcShare
- S0428: PoetRAT
- S0192: Pupy
- S0262: QuasarRAT
- S1209: Quick Assist
- S0332: Remcos
- S0379: Revenge RAT
- S0461: SDBbot
- S0098: T9000
- S0467: TajMahal
- S0670: WarzoneRAT
- S0412: ZxShell
- S0283: jRAT
- S0385: njRAT
