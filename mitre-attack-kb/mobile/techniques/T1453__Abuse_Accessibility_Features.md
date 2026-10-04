# T1453: Abuse Accessibility Features


**ATT&CK ID:** T1453  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1453  

## Description
Adversaries may abuse accessibility features in Android devices to steal sensitive data and to spread malware to other devices. Accessibility features in Android are designed to assist users with disabilities, performing a variety of tasks, such as using Action Blocks to control lightbulbs, and changing the device’s user interface, such as changing the font size and adjusting contract or colors.(Citation: Google_AndroidAcsOverview) 

One example of how adversaries abuse accessibility features is overlaying an HTML object mimicking a legitimate login screen. The user types their credentials in the overlay HTML object, which is then sent to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021)  

Another example is a malicious accessibility feature acting as a keylogger. The keylogger monitors changes on the EditText fields and sends it to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021) This method of attack is also described in [Keylogging](https://attack.mitre.org/techniques/T1417/001); whereas [Abuse Accessibility Features](https://attack.mitre.org/techniques/T1453) captures the overall abuse of accessibility features.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0422: Anubis
- S1083: Chameleon
- S1225: CherryBlos
- S9004: Crocodilus
- S9005: DocSwap
- S1067: FluBot
- S1231: GodFather
- S9006: VajraSpy
