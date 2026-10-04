# T1451: SIM Card Swap


**ATT&CK ID:** T1451  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1451  

## Description
Adversaries may gain access to mobile devices through transfers or swaps from victims’ phone numbers to adversary-controlled SIM cards and mobile devices.(Citation: ATT SIM Swap Scams)(Citation: Verizon SIM Swapping) 

The typical process is as follows:  

1. Adversaries will first gather information about victims through [Phishing](https://attack.mitre.org/techniques/T1660), social engineering, data breaches, or other avenues. 
2. Adversaries will then impersonate victims as they contact mobile carriers to request for the SIM swaps. For example, adversaries would provide victims’ name and address to mobile carriers; once authenticated, adversaries would request for victims’ phone numbers to be transferred to adversary-controlled SIM cards.  
3. Once completed, victims will lose mobile data, such as text messages and phone calls, on their mobile devices. In turn, adversaries will receive mobile data that was intended for the victims.  

Adversaries may use the intercepted SMS messages to log into online accounts that use SMS-based authentication. Specifically, adversaries may use SMS-based authentication to log into banking and/or cryptocurrency accounts, then transfer funds to adversary-controlled wallets.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Threat Groups Using This Technique
- G1004: LAPSUS$
- G1015: Scattered Spider
