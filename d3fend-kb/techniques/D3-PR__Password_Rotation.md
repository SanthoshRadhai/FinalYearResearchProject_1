# D3-PR: Password Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-PR/  

## Definition
Password rotation is a security policy that mandates the periodic change of user account passwords to mitigate the risk of unauthorized access due to compromised credentials.

## Parent Class(es)
- Credential Rotation

## Relationships
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Password

## Knowledge Base Article
## How it works

Users may be requested to change their passwords on a regular schedule. Management servers with enterprise policies for account management provide the ability to change or reset passwords for accounts.

## Considerations

Requiring users to change their passwords frequently can result in insecure password practices by the user. The latest update of NIST SP 800-63B, Digital Identity Guidelines, recommends requiring password reset only when a known compromise has occurred, or every 365 days, rather than every 60 or 90 days.
