# D3-CBAN: Certificate-based Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-CBAN/  

## Definition
Requiring a digital certificate in order to authenticate a user.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - Federal Public Key Infrastructure 101
- **reads:** Certificate

## Knowledge Base Article
## How it works

Certificate-based authentication is a security mechanism that uses digital certificates to verify the identity of a user, device, or server before granting access to a network or system. This method relies on a pair of cryptographic keys: a public key and a private key.

## Considerations

* Private Key Protection: Ensure that private keys are securely stored and protected against unauthorized access.
* Certificate Revocation: Implement a robust process for revoking certificates if they are compromised or no longer needed.
* Man-in-the Middle Attacks: Use mutual authentication to mitigate the risk of these attacks.
