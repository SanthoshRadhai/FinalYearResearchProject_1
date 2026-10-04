# D3-FRDDL: Forward Resolution Domain Denylisting

**Synonym(s):** Forward Resolution Domain Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-FRDDL/  

## Definition
Blocking a lookup based on the query's domain name value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works

Policies are created that filter DNS queries using fully qualified domain name (FQDN) of record in the query. A DNS policy can be created for blocking DNS queries from FQDNs that have been identified as unauthorized.

## Considerations

Continuous maintenance of unauthorized domain lists is needed to keep up to date as updates occur.
