# D3-CP: Certificate Pinning

**Reference:** https://d3fend.mitre.org/technique/D3-CP/  

## Definition
Persisting either a server's X.509 certificate or their public key and comparing that to server's presented identity to allow for greater client confidence in the remote server's identity for SSL connections.

## Parent Class(es)
- Credential Hardening

## Relationships
- **authenticates:** Public Key
- **hardens:** Certificate
- **kb-reference:** Reference - Certificate and Public Key Pinning
- **kb-reference:** Reference - End-to-end certificate pinning
- **kb-reference:** Reference - Public Key Pinning Extension for HTTP

## Knowledge Base Article
## How it works
Pinning allows for a trusted copy of a certificate or public key to be associated with a server and thus reducing the likelihood of frequently visited sites being subjected to man-in-the-middle attacks. Certificates or public keys can be pinned after a trusted connection has been established or the pinning can be preloaded in an application, which is the preferred method for mobile applications.

Pinning can take the form of certificate pinning or public key pinning.

## Forms of Pinning
* Certificate Pinning (CP) allows for the client to verify the X.509 certificate with a preloaded certificate. Typically, this is involves storing a hash of the certificate and using the stored hash for comparison to the hash of the certificate submitted during the SSL handshake.

* Public Key Pinning (PKP) requires the extraction of a public key from server's certificate. The stored public key is compared to the server's presented public key. A public key is expected to rotate less frequently than an X.509 certificate and is generally favored over certificate pinning.

An extension of PKP is Subject Public Key Information Pinning (SPKI) includes public key pinning plus additional information for SSL connections. The additional information can include preferred algorithms.

## Considerations

* With pinned certificates whenever a server updates its certificate, the pinned certificates will also need to be updated
* With pinned public keys the extracted key may be subject to key refresh policies but much less frequently
* Servers can become unavailable if pinned objects are set and not updated with the rotated identities. This may require a pinning strategy to be developed.
* The application of this technique within web browser applications has been [deprecated](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning) by  popular web browser developers. They now favor certificate analysis via public certificate transparency logs, and the EXPECT-CT HTTP header.
