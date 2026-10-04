# CWE-422: Unprotected Windows Messaging Channel ('Shatter')

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/422.html  

## Description
The product does not properly verify the source of a message in the Windows Messaging System while running at elevated privileges, creating an alternate channel through which an attacker can directly send a message to the product.

## Related Weaknesses
- ChildOf: CWE-420
- ChildOf: CWE-360

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Always verify and authenticate the source of the message.
