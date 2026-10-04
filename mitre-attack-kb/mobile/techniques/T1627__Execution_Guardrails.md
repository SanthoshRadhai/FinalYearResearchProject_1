# T1627: Execution Guardrails


**ATT&CK ID:** T1627  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1627  

## Description
Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. Values an adversary can provide about a target system or environment to use as guardrails may include environment information such as location.(Citation: SWB Exodus March 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [System Checks](https://attack.mitre.org/techniques/T1633/001). While use of [System Checks](https://attack.mitre.org/techniques/T1633/001) may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

## Sub-techniques
- T1627.001: Geofencing

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1215: Binary Validator
- S9005: DocSwap
