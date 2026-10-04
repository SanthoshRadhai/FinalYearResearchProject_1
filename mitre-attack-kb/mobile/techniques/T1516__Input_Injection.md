# T1516: Input Injection


**ATT&CK ID:** T1516  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1516  

## Description
A malicious application can inject input to the user interface to mimic user interaction through the abuse of Android's accessibility APIs.

[Input Injection](https://attack.mitre.org/techniques/T1516) can be achieved using any of the following methods:

* Mimicking user clicks on the screen, for example to steal money from a user's PayPal account.(Citation: android-trojan-steals-paypal-2fa)
* Injecting global actions, such as `GLOBAL_ACTION_BACK` (programatically mimicking a physical back button press), to trigger actions on behalf of the user.(Citation: Talos Gustuff Apr 2019)
* Inserting input into text fields on behalf of the user. This method is used legitimately to auto-fill text fields by applications such as password managers.(Citation: bitwarden autofill logins)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1094: BRATA
- S0480: Cerberus
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S0423: Ginp
- S1231: GodFather
- S0406: Gustuff
- S0485: Mandrake
- S0403: Riltok
- S1062: S.O.V.A.
- S1055: SharkBot
- S0545: TERRACOTTA
- S0427: TrickMo
- S0494: Zen
