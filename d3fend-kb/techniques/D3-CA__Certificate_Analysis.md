# D3-CA: Certificate Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-CA/  

## Definition
Analyzing Public Key Infrastructure certificates to detect if they have been misconfigured or spoofed using both network traffic, certificate fields and third-party logs.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Certificate File
- **kb-reference:** Reference - Securing Web Transactions

## Knowledge Base Article
## How it works
Certificate Analysis ensures that the data elements of the certificate are current and anchored in a known trust model. Certificate authorities, revocation lists, and third-party secure logs are used in the analysis. Analysis includes detection of server impersonation, phishing domains, and forged certificates.

TLS certificates are designed to expire to ensure that the cryptographic keys are forced to be changed on a regular basis. The certificates in the trust path also expire and can cause a break in the trust chain. This means that even if a server certificate is updated correctly, intermediate certificates can expire and the trust chain is not maintained. This can cause services to become unavailable.
