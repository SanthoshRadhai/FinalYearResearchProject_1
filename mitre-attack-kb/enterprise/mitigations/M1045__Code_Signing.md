# M1045: Code Signing

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1045  

## Description
Code Signing is a security process that ensures the authenticity and integrity of software by digitally signing executables, scripts, and other code artifacts. It prevents untrusted or malicious code from executing by verifying the digital signatures against trusted sources. Code signing protects against tampering, impersonation, and distribution of unauthorized or malicious software, forming a critical defense against supply chain and software exploitation attacks. This mitigation can be implemented through the following measures:

Enforce Signed Code Execution:

- Implementation: Configure operating systems (e.g., Windows with AppLocker or Linux with Secure Boot) to allow only signed code to execute.
- Use Case: Prevent the execution of malicious PowerShell scripts by requiring all scripts to be signed with a trusted certificate.

Vendor-Signed Driver Enforcement:

- Implementation: Enable kernel-mode code signing to ensure that only drivers signed by trusted vendors can be loaded.
- Use Case: A malicious driver attempting to modify system memory fails to load because it lacks a valid signature.

Certificate Revocation Management:

- Implementation: Use Online Certificate Status Protocol (OCSP) or Certificate Revocation Lists (CRLs) to block certificates associated with compromised or deprecated code.
- Use Case: A compromised certificate used to sign a malicious update is revoked, preventing further execution of the software.

Third-Party Software Verification:

- Implementation: Require software from external vendors to be signed with valid certificates before deployment.
- Use Case: An organization only deploys signed and verified third-party software to prevent supply chain attacks.

Script Integrity in CI/CD Pipelines:

- Implementation: Integrate code signing into CI/CD pipelines to sign and verify code artifacts before production release.
- Use Case: A software company ensures that all production builds are signed, preventing tampered builds from reaching customers.

**Key Components of Code Signing**

- Digital Signature Verification: Verifies the authenticity of code by ensuring it was signed by a trusted entity.
- Certificate Management: Uses Public Key Infrastructure (PKI) to manage signing certificates and revocation lists.
- Enforced Policy for Unsigned Code: Prevents the execution of unsigned or untrusted binaries and scripts.
- Hash Integrity Check: Confirms that code has not been altered since signing by comparing cryptographic hashes.

## Techniques Mitigated
- T1036: Masquerading
- T1036.001: Invalid Code Signature
- T1036.005: Match Legitimate Resource Name or Location
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.002: AppleScript
- T1127.002: ClickOnce
- T1204.003: Malicious Image
- T1505: Server Software Component
- T1505.001: SQL Stored Procedures
- T1505.002: Transport Agent
- T1505.004: IIS Components
- T1505.006: vSphere Installation Bundles
- T1525: Implant Internal Image
- T1543: Create or Modify System Process
- T1543.003: Windows Service
- T1546.006: LC_LOAD_DYLIB Addition
- T1546.013: PowerShell Profile
- T1554: Compromise Host Software Binary
- T1601: Modify System Image
- T1601.001: Patch System Image
- T1601.002: Downgrade System Image
