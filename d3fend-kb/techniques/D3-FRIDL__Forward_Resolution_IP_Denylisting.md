# D3-FRIDL: Forward Resolution IP Denylisting

**Synonym(s):** Forward Resolution IP Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-FRIDL/  

## Definition
Blocking a DNS lookup's answer's IP address value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Inbound Internet DNS Response Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works

This technique prevents a client from learning IP addresses deemed to be potentially malicious, which would have been delivered via forward resolution responses.

Responses to forward resolution requests (that is, requests where a domain is sent and IP(s) are returned) are collected, and the IP address(es) included as a response are examined. If the IP address(es) are in a range included in the blacklist, then the response is dropped and not forwarded to the client.

The DNS lookup can be blocked by either dropping the network traffic with an inline device, or modifying the value of the response sent by the DNS server. To transparently prevent client applications from hanging on a request, it is common practice to replace malicious values with addresses in the range 127.0.0.0/8 or the address of a honeypot maintained by the network administrators.

## Considerations

* This technique does not prevent the client from contacting the blacklisted IP, only from learning about this IP address via a nameserver lookup request.
* DNS Response traffic can be transmitted over many different protocols, which presents a challenge to implementing methods to extract all DNS answer IP address value(s).
  * DNS has historically used UDP port 53, with TCP port 53 instead used for responses over 512 bytes or after a lack of response over UDP.
  * Usage of new protocols to provide confidentiality for DNS traffic, such as DoH (DNS over HTTPS) and DoT (DNS over TLS), complicates collection of the IP address(es) in DNS responses. These protocols have often been enabled in browser settings transparently after a browser update, with DNS requests proxied over one of these cryptographic protocols through a specified host.
* This technique must be implemented logically between the application that receives the response and the server which sent the response.
  * DNS responses sent in an encrypted manner, such as those using DoH or DoT, will require interception of the TLS connections in order to determine the IP address(es) in the response.
* Replacing the response is not effective in the case that the nameserver uses a technique to provide integrity of its responses, such as DNSSEC for DNS responses.
