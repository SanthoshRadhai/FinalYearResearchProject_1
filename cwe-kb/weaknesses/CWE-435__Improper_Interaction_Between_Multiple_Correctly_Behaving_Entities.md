# CWE-435: Improper Interaction Between Multiple Correctly-Behaving Entities

**Abstraction:** Pillar  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/435.html  

## Description
An interaction error occurs when two entities have correct behavior when running independently of each other, but when they are integrated as components in a larger system or process, they introduce incorrect behaviors that may cause resultant weaknesses.

## Extended Description
When a system or process combines multiple independent components, this often produces new, emergent behaviors at the system level. However, if the interactions between these components are not fully accounted for, some of the emergent behaviors can be incorrect or even insecure.

## Common Consequences
- Scope: Integrity; Impact: Unexpected State, Varies by Context

## Demonstrative Examples (summary)
- The paper "Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection" [REF-428] shows that OSes varied widely in how they manage unusual packets, which made it difficult or impossible for intrusion detection systems to properly detect certain attacker manipulations that took advantage of these OS differences.
