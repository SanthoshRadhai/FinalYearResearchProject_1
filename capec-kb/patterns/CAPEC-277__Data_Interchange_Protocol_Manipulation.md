# CAPEC-277: Data Interchange Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/277.html  

## Description
Data Interchange Protocols are used to transmit structured data between entities. These protocols are often specific to a particular domain (B2B: purchase orders, invoices, transport logistics and waybills, medical records). They are often, but not always, XML-based. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Related Weaknesses (CWE)
- CWE-707
