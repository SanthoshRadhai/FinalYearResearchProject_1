# S9037: RustyWater

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9037  
**Aliases:** RustyWater, Archer RAT / RUSTRIC  
**Platforms:** Windows  

## Description
[RustyWater](https://attack.mitre.org/software/S9037) is a Rust-based implant used by [MuddyWater](https://attack.mitre.org/groups/G0069). Historically, [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell-based tools and [RustyWater](https://attack.mitre.org/software/S9037) reflects a shift in tooling, demonstrating better techniques for defense evasion and reverse engineering.(Citation: CloudSEK_RustyWater_Jan2026)

## Techniques Used
- T1027: Obfuscated Files or Information
- T1027.013: Encrypted/Encoded File
- T1033: System Owner/User Discovery
- T1036.005: Match Legitimate Resource Name or Location
- T1055.002: Portable Executable Injection
- T1071.001: Web Protocols
- T1082: System Information Discovery
- T1087.002: Domain Account
- T1106: Native API
- T1132.001: Standard Encoding
- T1140: Deobfuscate/Decode Files or Information
- T1204.002: Malicious File
- T1518.001: Security Software Discovery
- T1547.001: Registry Run Keys / Startup Folder
- T1559.001: Component Object Model
- T1566.001: Spearphishing Attachment
- T1573.001: Symmetric Cryptography
- T1622: Debugger Evasion
- T1678: Delay Execution
- T1684.001: Impersonation
