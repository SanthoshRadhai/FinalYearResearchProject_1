# D3-CRO: Credential Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-CRO/  

## Definition
Credential rotation is a security procedure in which authentication credentials, such as passwords, API keys, or certificates, are regularly changed or replaced to minimize the risk of unauthorized access.

## Parent Class(es)
- Credential Hardening

## Relationships
- **kb-reference:** Reference - Eviction Guidance for Networks Affected by the SolarWinds and Active Directory/M365 Compromise - CISA
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Credential

## Knowledge Base Article
## How it works

Credentials can be systematically changed at predetermined intervals or based on specific events.  Credentials such as user passwords may be rotated manually, but it is increasingly common to use an automated system to manage rotation of enterprise passwords, certificates and keys.

## Considerations

- Rotation of credentials must be managed carefully to avoid inadvertent service interruption
- Management servers with enterprise policies for account management provide the ability to change or reset passwords for accounts. Some organizations rotate credentials periodically to limit the risk of stolen credentials.
- When responding to an incident, severity of compromise should be considered to determine what credentials to what accounts should be regenerated
- If proactively rotating credentials periodically, several factors should be considered to determine the frequency. Also introduces some risk including promoting the creation of weak passwords and poor storage practices for employees and presents challenges in proper tracking.
