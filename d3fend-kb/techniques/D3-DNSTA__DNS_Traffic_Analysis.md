# D3-DNSTA: DNS Traffic Analysis

**Synonym(s):** Domain Name Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSTA/  

## Definition
Analysis of domain name metadata, including name and DNS records, to determine whether the domain is likely to resolve to an undesirable host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Domain age registration alert - Inc Rapid7 Inc RAPID7 Inc
- **kb-reference:** Reference - Heuristic botnet detection - Palo Alto Networks Inc
- **kb-reference:** Reference - Method and system for detecting algorithm-generated domains - VECTRA NETWORKS Inc
- **kb-reference:** Reference - Predicting Domain Generation Algorithms with Long Short-Term Memory Networks
- **kb-reference:** Reference - Sinkholing bad network domains by registering the bad network domains on the internet - Palo Alto Networks Inc
- **may-contain:** DNS Lookup

## Knowledge Base Article
## How it works
This technique can be accomplished in a number of ways.

* One example analytic determines whether or not a domain name was generated with an algorithm. Domain generation algorithms (DGAs) are sometimes used to create a domain name automatically  that will resolve to C2 infrastructure, without directly coding the domains in question into the malicious code.
* Another method analyzes information about domains that have been visited, including whether a domain name is longer than a common length,  if a dynamic DNS domain was visited, if a fast-flux domain was visited, and if a recently created domain was visited. These factors are used to develop a score and if that score is over a certain threshold, an alert is generated.
* Collected malware samples can be executed in a virtual environment to identify network domains that are connected to during execution. The network domains are then generated into signatures to identity bad domains for other hosts.

This technique does not check for content hosted at the domain.

## Considerations

* DNS produces a large amount of traffic which can be resource-intensive to analyze in real time.
* If a server is compromised, for example, as part of a watering hole attack, but the DNS information pointing to that server is not altered, this technique would not catch such an incident.
