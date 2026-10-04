# D3-HDL: Homoglyph Denylisting

**Synonym(s):** Homoglyph Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-HDL/  

## Definition
Blocking DNS queries that are deceptively similar to legitimate domain names.

## Parent Class(es)
- Forward Resolution Domain Denylisting

## Relationships
- **kb-reference:** Reference - Detection of Malicious IDNHomoglyph Domains

## Knowledge Base Article
## How it works

Homoglyph domain blacklisting considers the domain and subdomain structure of a lookup and compares the named components to blacklisted named components. The blacklisted named components are typically crafted modifications of known good domains, e.g., gooogle.com versus google.com. The blacklisted domains typically resemble trusted domains, but have been altered slightly to deceive users.

The blacklisted named components also include consideration for fonts or Unicode characters that can make certain characters appear very similar (zero vs capital O and the letter l vs the number one). The blacklisted domains under certain fonts will appear to be a trusted domain.

## Considerations
* Maintaining the currency of the list can be a challenge especially with newly registered domain entries.
* Blacklists should have identified maintenance cycles to ensure lists are not stale.
