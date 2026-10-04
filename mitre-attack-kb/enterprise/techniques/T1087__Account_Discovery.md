# T1087: Account Discovery


**ATT&CK ID:** T1087  
**Domain:** Mitre Attack  
**Tactic(s):** Discovery  
**Platforms:** ESXi, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1087  

## Description
Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List Users)(Citation: Google Cloud - IAM Servie Accounts List API) On hosts, adversaries can use default [PowerShell](https://attack.mitre.org/techniques/T1059/001) and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Sub-techniques
- T1087.001: Local Account
- T1087.002: Domain Account
- T1087.003: Email Account
- T1087.004: Cloud Account

## Mitigations
- M1018: User Account Management
- M1028: Operating System Configuration

## Known Threat Groups Using This Technique
- G0143: Aquatic Panda
- G1016: FIN13
- G1015: Scattered Spider

## Known Software Using This Technique
- S1229: Havoc
- S0445: ShimRatReporter
- S1239: TONESHELL
- S1065: Woody RAT
- S0658: XCSSET
