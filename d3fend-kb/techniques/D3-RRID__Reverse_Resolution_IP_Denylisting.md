# D3-RRID: Reverse Resolution IP Denylisting

**Synonym(s):** Reverse Resolution IP Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-RRID/  

## Definition
Blocking a reverse lookup based on the query's IP address value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
This technique prevents a client from learning domains deemed to be potentially malicious, which would have been delivered via reverse resolution responses over the DNS protocol.

Queries for reverse resolution requests (that is, requests where IP(s) are sent and a domain is returned) are collected, and the IP address(es) included in the query are examined. If the IP address(es) are in a range included in the blacklist, then the query is dropped.

## Considerations
- The blacklist will have to be maintained and will need to be kept up to date with identified maintenance cycles to ensure lists are not stale.
- DNS query traffic can be transmitted over many different protocols, which presents a challenge to implementing methods to extract all DNS query IP address value(s).
  - DNS has historically used UDP port 53, with TCP port 53 instead used for responses over 512 bytes or after a lack of response over UDP.
  - Usage of new protocols to provide confidentiality for DNS traffic, such as DoH (DNS over HTTPS) and DoT (DNS over TLS), complicates collection of the IP address(es) in DNS queries. These protocols have often been enabled in browser settings transparently after a browser update, with DNS queries proxied over one of these cryptographic protocols through a specified host.
