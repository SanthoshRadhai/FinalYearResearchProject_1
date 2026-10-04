# D3-ANCI: Authentication Cache Invalidation

**Reference:** https://d3fend.mitre.org/technique/D3-ANCI/  

## Definition
Removing tokens or credentials from an authentication cache to prevent further user associated account accesses.

## Parent Class(es)
- Credential Eviction

## Relationships
- **deletes:** Credential
- **kb-reference:** Reference - Secure caching of server credentials - Dell Products LP
- **kb-reference:** Reference - System and method for providing an actively invalidated client-side network resource cache - IMVU

## Knowledge Base Article
## How it works
Applications can locally cache user authentication credentials for certain server connections. An application may attempt to use the cached credential for a connection. If the cached credentials exist then the user will not be typically prompted for new credentials.


## Considerations
Are these cached credentials only on the local host? Can they be persisted to the remote server?

## Examples
Windows Credential Management API
