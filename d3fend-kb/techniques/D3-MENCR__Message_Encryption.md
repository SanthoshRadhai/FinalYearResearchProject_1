# D3-MENCR: Message Encryption

**Reference:** https://d3fend.mitre.org/technique/D3-MENCR/  

## Definition
Encrypting a message body using a cryptographic key.

## Parent Class(es)
- Message Hardening

## Relationships
- **encrypts:** Digital Message
- **kb-reference:** Reference - Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.1

## Knowledge Base Article
## How it works

### Asymmetric Cryptography
Asymmetric encryption is typically accomplished using public and private key certificates based on the X.509 standard. The sender encrypts messages using the recipient's public key and the receipt decrypts the message using their private key. Standards that can be used to implement user message encryption include S/MIME (Secure/Multipurpose Internet Mail Extensions) and PGP.

### Symmetric Cryptography
Symmetric encryption uses the same cryptographic key by both the sender and receiver to encrypt and decrypt a message. Asymmetric key exchange protocols such as Diffie-Hellman can be used to share the cryptographic key with the recipient. For synchronous or low-latency environments (like a message bus), a pre-shared or dynamically derived symmetric key is typically used to minimize computational overhead.

## Considerations
- Separate configuration settings to enable message encryption are often needed for each messenger client (e.g. webmail, desktop client, mobile).
- Continuous monitoring to ensure private keys are not compromised and the certificate authority (CA) is trusted.
- Secure transfer of private keys between multiple devices.
- Encryption adds latency and increases CPU utilization; while negligible for user-to-user messages, it can be a critical factor for real-time bus systems.
