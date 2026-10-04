# T1643: Generate Traffic from Victim


**ATT&CK ID:** T1643  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1643  

## Description
Adversaries may generate outbound traffic from devices. This is typically performed to manipulate external outcomes, such as to achieve carrier billing fraud or to manipulate app store rankings or ratings. Outbound traffic is typically generated as SMS messages or general web traffic, but may take other forms as well.

If done via SMS messages, Android apps must hold the `SEND_SMS` permission. Additionally, sending an SMS message requires user consent if the recipient is a premium number. Applications cannot send SMS messages on iOS

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0440: Agent Smith
- S0525: Android/AdDisplay.Ashas
- S0293: BrainTest
- S0432: Bread
- S1103: FlixOnline
- S0290: Gooligan
- S0322: HummingBad
- S0321: HummingWhale
- S0325: Judy
- S0303: MazarBOT
- S0291: PJApps
- S0326: RedDrop
- S0419: SimBad
- S0545: TERRACOTTA
- S0424: Triada
- S0494: Zen
