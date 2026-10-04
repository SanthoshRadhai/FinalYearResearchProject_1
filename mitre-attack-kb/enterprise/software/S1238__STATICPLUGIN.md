# S1238: STATICPLUGIN

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1238  
**Aliases:** STATICPLUGIN  
**Platforms:** Windows  

## Description
[STATICPLUGIN](https://attack.mitre.org/software/S1238) is a downloader known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) has utilized a valid certificate in order to bypass endpoint security protections.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) masqueraded as legitimate software installer by using a custom TForm.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) has been leveraged to deploy a loader that facilitates follow on malware.(Citation: Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025)

## Techniques Used
- T1036.005: Match Legitimate Resource Name or Location
- T1036.008: Masquerade File Type
- T1204.002: Malicious File
- T1553.002: Code Signing
- T1559.001: Component Object Model
