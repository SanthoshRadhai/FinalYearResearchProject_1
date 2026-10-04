# D3-CS: Credential Scrubbing

**Reference:** https://d3fend.mitre.org/technique/D3-CS/  

## Definition
The systematic removal of hard-coded credentials from source code to prevent accidental exposure and unauthorized access.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Subroutine
- **kb-reference:** Secrets Management Cheat Sheet

## Knowledge Base Article
## How it Works
Credential Scrubbing involves identifying and eliminating hard-coded credentials such as usernames, passwords, API keys, and tokens from source code repositories. These credentials should be managed securely using environment variables, secret management tools, or secure vaults where they can be safely accessed when needed.

## Considerations
* Developers should conduct regular audits of source code to ensure credentials are not hard-coded.
* Exposed credentials found in version control history must be disabled and replaced promptly.
* Adopt role-based access controls and credential rotation policies to minimize security risks.
