# CAPEC-621: Analysis of Packet Timing and Sizes

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/621.html  

## Description
An attacker may intercept and log encrypted transmissions for the purpose of analyzing metadata such as packet timing and sizes. Although the actual data may be encrypted, this metadata may reveal valuable information to an attacker. Note that this attack is applicable to VOIP data as well as application data, especially for interactive apps that require precise timing and low-latency (e.g. thin-clients).

## Related Attack Patterns
- ChildOf: CAPEC-189

## Prerequisites
- Use of untrusted communication paths enables an attacker to intercept and log communications, including metadata such as packet timing and sizes.

## Skills Required
- [High] These attacks generally require sophisticated machine learning techniques and require traffic capture as a prerequisite.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Distort packet sizes and timing at VPN layer by adding padding to normalize packet sizes and timing delays to reduce information leakage via timing.

## Related Weaknesses (CWE)
- CWE-201
