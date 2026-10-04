# D3-IAA: Identifier Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IAA/  

## Definition
Taking known malicious identifiers and determining if they are present in a system.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** Identifier
- **kb-reference:** Reference - The Pyramid of Pain - David Bianco

## Knowledge Base Article
## How it works

Identifier activity analysis is the process of taking identifiers--typically known malicious identifiers--and determining the artifacts that have interacted with those identifiers.

There are many open and closed source repositories of identifiers that represent indicators of compromise. For example, VirusTotal contains hash signatures of malware and IP Addresses used by threat actors. Defenders can search for these indicators of compromise their own systems to gain context on activity around an identifier.

## Considerations

Indicator activity analysis is a good way to gain high precision analysis, but adversaries can modify their own signatures such as hashes quickly to evade detection. This is related to David Bianco’s Pyramid of Pain - Indicators on the lower level (hash values, IP addresses domain names) are easy for adversaries to change.

Identifier activity data of interest for analysis with the identifier might include, but is not limited to:

* network traffic activity where the identifier was used to identify communicating entities or referred to in the communication
* process activity referencing the identifier, especially for resource access
* file activity referencing the identifier
* registry settings referencing the identifier
