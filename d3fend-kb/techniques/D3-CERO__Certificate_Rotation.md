# D3-CERO: Certificate Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-CERO/  

## Definition
Certificate rotation involves replacing digital certificates and their private keys to maintain cryptographic integrity and trust, mitigating key compromise risks and ensuring continuous secure communications.

## Parent Class(es)
- Credential Rotation

## Relationships
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Certificate

## Knowledge Base Article
## How it works

Certificate rotation should be performed when:
- Any certificate expires.
- A new CA authority is substituted for the old, thus requiring a replacement root certificate.
- New or modified constraints need to be imposed on one or more certificates.
- A security breach has occurred.

Considerations:
- Managing certificate rotation across an enterprise can be complex. Automated solutions, sold by multiple vendors, should be considered to manage this complexity.
