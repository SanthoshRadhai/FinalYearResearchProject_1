# CAPEC-162: Manipulating Hidden Fields

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/162.html  

## Description
An adversary exploits a weakness in the server's trust of client-side processing by modifying data on the client-side, such as price information, and then submitting this data to the server, which processes the modified data. For example, eShoplifting is a data manipulation attack against an on-line merchant during a purchasing transaction. The manipulation of price, discount or quantity fields in the transaction message allows the adversary to acquire items at a lower cost than the merchant intended. The adversary performs a normal purchasing transaction but edits hidden fields within the HTML form response that store price or other information to give themselves a better deal. The merchant then uses the modified pricing information in calculating the cost of the selected items.

## Related Attack Patterns
- ChildOf: CAPEC-77

## Prerequisites
- The targeted site must contain hidden fields to be modified.
- The targeted site must not validate the hidden fields with backend processing.

## Resources Required
- The adversary must have the ability to modify hidden fields by editing the HTTP response to the server.

## Related Weaknesses (CWE)
- CWE-602
