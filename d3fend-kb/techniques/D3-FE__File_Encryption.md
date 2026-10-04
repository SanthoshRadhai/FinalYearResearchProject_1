# D3-FE: File Encryption

**Reference:** https://d3fend.mitre.org/technique/D3-FE/  

## Definition
Encrypting a file using a cryptographic key.

## Parent Class(es)
- Platform Hardening

## Relationships
- **encrypts:** File
- **kb-reference:** Reference -  File Encryption 101: Safeguarding Your Sensitive Data
- **kb-reference:** Reference - Guide to Storage Encryption Technologies for End User Devices
- **kb-reference:** Reference - Security Considerations for Exchanging Files Over the Internet

## Knowledge Base Article
## How it Works
Files are encrypted using either a single key for both encryption and decryption or separate keys. Single key encryption is symmetric encryption and using two key distinct keys is asymmetric encryption.

### Symmetric Cryptography
Symmetric encryption uses the same cryptographic key for both the encryption and decryption a file. Managing keys at scale sometimes uses asymmetric key exchange. Protocols such as RSA or Diffie-Hellman can be used to share the symmetric cryptographic key with the others.

### Asymmetric Cryptography
Asymmetric encryption is typically accomplished using public and private key certificates based on the X.509 standard. Files are encrypted using the public key and decrypted using their private key. Asymmetric encryption is typically slower than symmetric encryption and not widely used for large file encryption, but is popular for key wrapping, key exchanges, and digital signatures.

## Considerations
- Continuous monitoring must be carried out to ensure private keys are not compromised and the certificate authority (CA) is trusted.
- Transfer of private keys between multiple devices must be performed securely.
