# T1217: Browser Information Discovery


**ATT&CK ID:** T1217  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1217  

## Description
Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [Credentials In Files](https://attack.mitre.org/techniques/T1552/001) associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)

## Known Threat Groups Using This Technique
- G0082: APT38
- G0114: Chimera
- G0117: Fox Kitten
- G0094: Kimsuky
- G1036: Moonstone Sleet
- G1015: Scattered Spider
- G1017: Volt Typhoon

## Known Software Using This Technique
- S1246: BeaverTail
- S0274: Calisto
- S1153: Cuckoo Stealer
- S0673: DarkWatchman
- S0567: Dtrack
- S0363: Empire
- S9010: GlassWorm
- S1185: LightSpy
- S0681: Lizar
- S1213: Lumma Stealer
- S0409: Machete
- S1060: Mafalda
- S1122: Mispadu
- S0079: MobileOrder
- S1012: PowerLess
- S1240: RedLine Stealer
- S1042: SUGARDUMP
- S1196: Troll Stealer
