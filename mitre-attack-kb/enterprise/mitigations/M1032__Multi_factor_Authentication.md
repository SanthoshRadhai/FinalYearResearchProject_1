# M1032: Multi-factor Authentication

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1032  

## Description
Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include:

- *Something you know*: Passwords, PINs.
- *Something you have*: Physical tokens, smartphone authenticator apps.
- *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans.

Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures:

Identity and Access Management (IAM):

- Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles.
- Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations).
- Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra.

Authentication Tools and Methods:

- Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP).
- Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security.
- Enforce biometric authentication for compatible devices and applications.

Secure Legacy Systems:

- Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet.
- Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins.

Monitoring and Alerting:

- Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems.
- Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations.

Training and Policy Enforcement:

- Educate employees on the importance of MFA and secure authenticator usage.
- Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

## Techniques Mitigated
- T1021: Remote Services
- T1021.001: Remote Desktop Protocol
- T1021.004: SSH
- T1021.007: Cloud Services
- T1040: Network Sniffing
- T1072: Software Deployment Tools
- T1078: Valid Accounts
- T1078.001: Default Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1098.002: Additional Email Delegate Permissions
- T1098.003: Additional Cloud Roles
- T1098.005: Device Registration
- T1098.006: Additional Container Cluster Roles
- T1110: Brute Force
- T1110.001: Password Guessing
- T1110.002: Password Cracking
- T1110.003: Password Spraying
- T1110.004: Credential Stuffing
- T1114: Email Collection
- T1114.002: Remote Email Collection
- T1133: External Remote Services
- T1136: Create Account
- T1136.001: Local Account
- T1136.002: Domain Account
- T1136.003: Cloud Account
- T1199: Trusted Relationship
- T1213: Data from Information Repositories
- T1213.003: Code Repositories
- T1485: Data Destruction
- T1530: Data from Cloud Storage
- T1539: Steal Web Session Cookie
- T1556: Modify Authentication Process
- T1556.001: Domain Controller Authentication
- T1556.003: Pluggable Authentication Modules
- T1556.004: Network Device Authentication
- T1556.006: Multi-Factor Authentication
- T1556.007: Hybrid Identity
- T1599: Network Boundary Bridging
- T1599.001: Network Address Translation Traversal
- T1601: Modify System Image
- T1601.001: Patch System Image
- T1601.002: Downgrade System Image
- T1621: Multi-Factor Authentication Request Generation
- T1669: Wi-Fi Networks
