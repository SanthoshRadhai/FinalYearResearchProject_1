# D3-DNSCE: DNS Cache Eviction

**Synonym(s):** Flush DNS Cache  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSCE/  

## Definition
Flushing DNS to clear any IP addresses or other DNS records from the cache.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** DNS Record
- **kb-reference:** Reference - Eviction Guidance for Networks Affected by the SolarWinds and Active Directory/M365 Compromise - CISA

## Knowledge Base Article
# How it works

Flushing the DNS Cache will clear the IP addresses of websites you have visited recently. This can help remediate DNS Cache Poisoning attacks, which is a type of cyber attack where corrupted DNS data is inserted into the cache, causing redirects to malicious websites.

On windows, the DNS cache can be wiped by issuing the command `ipconfig /flushdns`.
