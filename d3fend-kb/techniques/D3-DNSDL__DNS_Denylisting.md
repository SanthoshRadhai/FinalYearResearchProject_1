# D3-DNSDL: DNS Denylisting

**Synonym(s):** DNS Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSDL/  

## Definition
Blocking DNS Network Traffic based on criteria such as IP address, domain name, or DNS query type.

## Parent Class(es)
- Network Isolation

## Relationships
- **blocks:** DNS Network Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
Rules are implemented that filter DNS queries using criteria such as:
- Client subnet
- Type of network protocol used in query
- Fully qualified domain name (FQDN) of record in the query
- DNS Server IP address that received the DNS request
- Type of DNS record being queried
- Time of day the query is received
- Size of the response

For example, a DNS policy can be created for blocking DNS queries for FQDNs that have been identified as unauthorized.

## Considerations
- Implementation considerations for DNS filtering policies to avoid over-blocking or under-blocking domains.
- Continuous maintenance of unauthorized domain lists is needed to keep up to date with possible site content changes.
- File sharing or content delivery networks may require other filtering techniques that are more fine-grained (URL blocking).
- Access to malicious websites or other network resources directly by IP instead of by DNS record, or after alteration of local DNS hosts file, may not result in DNS network traffic.
