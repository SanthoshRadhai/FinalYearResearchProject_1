# D3-TB: Token Binding

**Reference:** https://d3fend.mitre.org/technique/D3-TB/  

## Definition
Token binding is a security mechanism used to enhance the protection of tokens, such as cookies or OAuth tokens, by binding them to a specific connection.

## Parent Class(es)
- Credential Hardening

## Relationships
- **kb-reference:** Reference - The Token Binding Protocol Version 1.0
- **strengthens:** Access Token

## Knowledge Base Article
## How it works

When issuing a security token to a client that supports Token Binding, a server includes the client's Token Binding ID (or its cryptographic hash) in the token. Later on, when a client presents a security token containing a Token Binding ID, the server verifies that the ID in the token matches the ID of the Token Binding established with the client. In the case of a mismatch, the server rejects the token.

## Considerations

- While industry participation in the standards process is widespread, browser support remains limited.
- In practice, token-binding implementations are tied to Transport Security Layer (TLS).
