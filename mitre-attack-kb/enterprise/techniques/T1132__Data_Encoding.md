# T1132: Data Encoding


**ATT&CK ID:** T1132  
**Domain:** Mitre Attack  
**Tactic(s):** Command And Control  
**Platforms:** ESXi, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1132  

## Description
Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

## Sub-techniques
- T1132.001: Standard Encoding
- T1132.002: Non-Standard Encoding

## Mitigations
- M1031: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G1047: Velvet Ant

## Known Software Using This Technique
- S0128: BADNEWS
- S0132: H1N1
- S9035: LAMEHUG
- S0362: Linux Rabbit
- S0699: Mythic
- S0386: Ursnif
- S9003: evilginx2
