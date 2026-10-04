# CWE-295: Improper Certificate Validation

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/295.html  

## Description
The product does not validate, or incorrectly validates, a certificate.

## Related Weaknesses
- ChildOf: CWE-287
- ChildOf: CWE-287
- PeerOf: CWE-322

## Common Consequences
- Scope: Integrity, Authentication; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — When a certificate is invalid or malicious, it might allow an attacker to spoof a trusted entity by interfering in the communication path between the host and client. The product might connect to a malicious host while believing it is a trusted host, or the product might be deceived into accepting spoofed data that appears to originate from a trusted host.

## Potential Mitigations
- [Architecture and Design, Implementation] Certificates should be carefully managed and checked to assure that data are encrypted with the intended owner's public key.
- [Implementation] If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

## Detection Methods
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Bytecode Weakness Analysis - including disassembler + source code weakness analysis Binary Weakness Analysis - including disassembler + source code weakness analysis
- [Manual Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Binary / Bytecode disassembler - then use manual analysis for vulnerabilities & anomalies
- [Dynamic Analysis with Automated Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Web Application Scanner
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Man-in-the-middle attack tool
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Focused Manual Spotcheck - Focused manual analysis of source Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Source code Weakness Analyzer Context-configured Source Code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- This code checks the certificate of a connected peer.
- The following OpenSSL code obtains a certificate and verifies it.
- The following OpenSSL code ensures that there is a certificate and allows the use of expired certificates.
- The following OpenSSL code ensures that there is a certificate before continuing execution.
- The following OpenSSL code ensures that the host has a certificate.
