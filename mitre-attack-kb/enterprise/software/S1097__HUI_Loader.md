# S1097: HUI Loader

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1097  
**Aliases:** HUI Loader  
**Platforms:** Windows  

## Description
[HUI Loader](https://attack.mitre.org/software/S1097) is a custom DLL loader that has been used since at least 2015 by China-based threat groups including [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) and [menuPass](https://attack.mitre.org/groups/G0045) to deploy malware on compromised hosts. [HUI Loader](https://attack.mitre.org/software/S1097) has been observed in campaigns loading [SodaMaster](https://attack.mitre.org/software/S0627), [PlugX](https://attack.mitre.org/software/S0013), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Komplex](https://attack.mitre.org/software/S0162), and several strains of ransomware.(Citation: SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022)

## Techniques Used
- T1140: Deobfuscate/Decode Files or Information
- T1574.001: DLL
- T1685: Disable or Modify Tools
