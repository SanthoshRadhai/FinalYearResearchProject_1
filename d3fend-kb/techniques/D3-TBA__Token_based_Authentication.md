# D3-TBA: Token-based Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-TBA/  

## Definition
Token-based authentication is an authentication protocol where users verify their identity in exchange for a unique access token. Users can then access the website, application, or resource for the life of the token without having to re-enter their credentials.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - Identity Providers: What is Token Based Authentication
- **uses:** Access Token

## Knowledge Base Article
## How it works

Token-based authentication starts with a user logging into a system, device or application, typically using a password or a security question. An authorization server validates that initial authentication and then issues an access token, which is a small piece of data that lets a client application make a secure call or signal to an API server. Once this initial token-based authentication protocol is completed, the token works like a stamped ticket: The user can continue to seamlessly access the relevant resources, without re-authenticating, for the duration of the token lifecycle. That lifecycle ends when the user logs out or quits an app — and can also be triggered by a set time-out protocol.

## Considerations:

While token-based authentication is undoubtedly a major step above traditional password-based authentication, the token is still considered a “bearer token” — that is, access is granted to whomever holds the token.
