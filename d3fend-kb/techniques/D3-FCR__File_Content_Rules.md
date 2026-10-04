# D3-FCR: File Content Rules

**Synonym(s):** File Content Signatures, File Signatures  
**Reference:** https://d3fend.mitre.org/technique/D3-FCR/  

## Definition
Employing a pattern matching rule language to analyze the content of files.

## Parent Class(es)
- File Content Analysis

## Relationships
- **kb-reference:** Reference - Computational modeling and classification of data streams - Crowdstrike Inc
- **kb-reference:** Reference - Detecting script-based malware - Crowdstrike Inc
- **kb-reference:** Reference - Distributed meta-information query in a network - Bit 9 Inc
- **kb-reference:** Reference - System and methods thereof for logical identification of malicious threats across a plurality of end-point devices (epd) communicatively connected by a network - Palo Alto Networks IncCyber Secdo Ltd

## Knowledge Base Article
## How it works
Rules, often called signatures, are used for both generic and targeted malware detection. The rules are usually expressed in a domain specific language (DSL), then deployed to software that scans files for matches. The rules are developed and broadly distributed by commercial vendors, or they are developed and deployed by enterprise security teams to address highly targeted or custom malware. Conceptually, there are public and private rule sets. Both leverage the same technology, but they are intended to detect different types of cyber adversaries.

## Considerations
* Patterns expressed in the DSLs range in their complexity. Some scanning engines support file parsing and normalization for high fidelity matching, others support only simple regular expression matching against raw file data. Engineers must make a trade-off in terms of:
     * The fidelity of the matching capabilities in order to balance high recall with avoiding false positives,
     * The computational load for scanning, and
     * The resilience of the engine to deal with adversarial content presented in different forms-- content which in some cases is designed to exploit or defeat the scanning engines.
 * Signature libraries can become large over time and impact scanning performance.
 * Some vendors who sell signatures have to delete old signatures over time.
 * Simple signatures against raw content cannot match against encoded, encrypted, or sufficiently obfuscated content.

## Implementations
 * YARA
 * ClamAV
