# T1634: Credentials from Password Store


**ATT&CK ID:** T1634  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access  
**Platforms:** iOS  
**Reference:** https://attack.mitre.org/techniques/T1634  

## Description
Adversaries may search common password storage locations to obtain user credentials. Passwords can be stored in several places on a device, depending on the operating system or application holding the credentials. There are also specific applications that store passwords to make it easier for users to manage and maintain. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Sub-techniques
- T1634.001: Keychain

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method
