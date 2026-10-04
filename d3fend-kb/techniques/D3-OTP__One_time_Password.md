# D3-OTP: One-time Password

**Synonym(s):** OTP  
**Reference:** https://d3fend.mitre.org/technique/D3-OTP/  

## Definition
A one-time password is valid for only one user authentication.

## Parent Class(es)
- Password Rotation

## Relationships
- **kb-reference:** Reference - Digital Identity Guidelines 800-63-3
- **kb-reference:** Reference - RFC 2289 - A One-Time Password System
- **use-limits:** Password

## Knowledge Base Article
## How it works

When a user initiates authentication, they are asked for a one-time password, often in addition to other credentials such as a traditional password or smart card. The one-time password may be from a list provided in advance, sent via a channel such as SMS or HTTPS to an app, or a generated token.

In the case of a physical token which generates one-time passwords incrementally based on time elapsed, that token device need not be connected to the internet. In different implementations, an administrator of the system, or a user with additional verification, can adjust for clock skew between the token and the verification system as needed.

## Considerations

### Compromise of delivery channel
- SIM Swapping
- Secure token visual compromise
- Insecure delivery channel

### Compromise of delivery device
Physical loss of One-time Password device.

### Compromise of long-term backup codes
These are often provided in the form of a downloadable document with a regular name, which can be searched for in the case that the user forgets where they put them.  This digital file or printed document could be stolen.
Additionally, after the code file is printed, it could be recovered from the system printer spool unless the spooler cache is cleared.
