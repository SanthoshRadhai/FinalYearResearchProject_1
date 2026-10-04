# S9033: Fooder

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9033  
**Aliases:** Fooder  
**Platforms:** Windows  

## Description
[Fooder](https://attack.mitre.org/software/S9033) is a custom 64-bit C/C++ loader used by [MuddyWater](https://attack.mitre.org/groups/G0069) that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the [MuddyViper](https://attack.mitre.org/software/S9032) backdoor. [Fooder](https://attack.mitre.org/software/S9033) has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).(Citation: ESET_MuddyWater_Dec2025)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1036.005: Match Legitimate Resource Name or Location
- T1106: Native API
- T1134.001: Token Impersonation/Theft
- T1140: Deobfuscate/Decode Files or Information
- T1620: Reflective Code Loading
- T1678: Delay Execution
