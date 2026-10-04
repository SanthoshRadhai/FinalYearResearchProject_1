# S0002: Mimikatz

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0002  
**Aliases:** Mimikatz  
**Platforms:** Windows  

## Description
[Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide)

## Techniques Used
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.004: LSA Secrets
- T1003.006: DCSync
- T1098: Account Manipulation
- T1134.005: SID-History Injection
- T1207: Rogue Domain Controller
- T1547.005: Security Support Provider
- T1550.002: Pass the Hash
- T1550.003: Pass the Ticket
- T1552.004: Private Keys
- T1555: Credentials from Password Stores
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1558.001: Golden Ticket
- T1558.002: Silver Ticket
- T1649: Steal or Forge Authentication Certificates
