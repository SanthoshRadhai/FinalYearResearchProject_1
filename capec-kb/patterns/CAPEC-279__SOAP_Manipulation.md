# CAPEC-279: SOAP Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/279.html  

## Description
Simple Object Access Protocol (SOAP) is used as a communication protocol between a client and server to invoke web services on the server. It is an XML-based protocol, and therefore suffers from many of the same shortcomings as other XML-based protocols. Adversaries can make use of these shortcomings and manipulate the content of SOAP paramters, leading to undesirable behavior on the server and allowing the adversary to carry out a number of further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-278
- CanPrecede: CAPEC-110
- CanPrecede: CAPEC-228

## Prerequisites
- An application uses SOAP-based web service api.
- An application does not perform sufficient input validation to ensure that user-controllable data is safe for an XML parser.
- The targeted server either fails to verify that data in SOAP messages conforms to the appropriate XML schema, or it fails to correctly handle the complete range of data allowed by the schema.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-707
