# TA0006: Credential Access

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0006  

## Description
The adversary is trying to steal account names and passwords.

Credential Access consists of techniques for stealing credentials like account names and passwords. Techniques used to get credentials include keylogging or credential dumping. Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals.

## Techniques in This Tactic
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1003.002: Security Account Manager
- T1003.003: NTDS
- T1003.004: LSA Secrets
- T1003.005: Cached Domain Credentials
- T1003.006: DCSync
- T1003.007: Proc Filesystem
- T1003.008: /etc/passwd and /etc/shadow
- T1040: Network Sniffing
- T1056: Input Capture
- T1056.001: Keylogging
- T1056.002: GUI Input Capture
- T1056.003: Web Portal Capture
- T1056.004: Credential API Hooking
- T1110: Brute Force
- T1110.001: Password Guessing
- T1110.002: Password Cracking
- T1110.003: Password Spraying
- T1110.004: Credential Stuffing
- T1111: Multi-Factor Authentication Interception
- T1187: Forced Authentication
- T1212: Exploitation for Credential Access
- T1528: Steal Application Access Token
- T1539: Steal Web Session Cookie
- T1552: Unsecured Credentials
- T1552.001: Credentials In Files
- T1552.002: Credentials in Registry
- T1552.003: Shell History
- T1552.004: Private Keys
- T1552.005: Cloud Instance Metadata API
- T1552.006: Group Policy Preferences
- T1552.007: Container API
- T1552.008: Chat Messages
- T1555: Credentials from Password Stores
- T1555.001: Keychain
- T1555.002: Securityd Memory
- T1555.003: Credentials from Web Browsers
- T1555.004: Windows Credential Manager
- T1555.005: Password Managers
- T1555.006: Cloud Secrets Management Stores
- T1556: Modify Authentication Process
- T1556.001: Domain Controller Authentication
- T1556.002: Password Filter DLL
- T1556.003: Pluggable Authentication Modules
- T1556.004: Network Device Authentication
- T1556.005: Reversible Encryption
- T1556.006: Multi-Factor Authentication
- T1556.007: Hybrid Identity
- T1556.008: Network Provider DLL
- T1556.009: Conditional Access Policies
- T1557: Adversary-in-the-Middle
- T1557.001: Name Resolution Poisoning and SMB Relay
- T1557.002: ARP Cache Poisoning
- T1557.003: DHCP Spoofing
- T1557.004: Evil Twin
- T1558: Steal or Forge Kerberos Tickets
- T1558.001: Golden Ticket
- T1558.002: Silver Ticket
- T1558.003: Kerberoasting
- T1558.004: AS-REP Roasting
- T1558.005: Ccache Files
- T1606: Forge Web Credentials
- T1606.001: Web Cookies
- T1606.002: SAML Tokens
- T1621: Multi-Factor Authentication Request Generation
- T1649: Steal or Forge Authentication Certificates
