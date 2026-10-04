# D3-HDDL: Hierarchical Domain Denylisting

**Synonym(s):** Hierarchical Domain Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-HDDL/  

## Definition
Blocking the resolution of any subdomain of a specified domain name.

## Parent Class(es)
- Forward Resolution Domain Denylisting

## Relationships
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
This technique is used to block DNS queries from related domains and subdomains that are unauthorized.

Hierarchical domain blacklisting considers the blacklisting of second level domains and additional sub-domains and specific hosts for a given query value. A denylist is maintained that contains DNS names and corresponding subdomains, including wildcards, that should be blocked for a given lookup.

## Considerations
* The denylist of domain names will have to be maintained and will need to be kept up to date
* Other domains that resolve to the domain of interest for blocking (CNAME, etc).
* Denylists should have identified maintenance cycles to ensure lists are not stale.
