# CWE-603: Use of Client-Side Authentication

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/603.html  

## Description
A client/server product performs authentication within client code but not in server code, allowing server-side authentication to be bypassed via a modified client that omits the authentication check.

## Extended Description
Client-side authentication is extremely weak and may be breached easily. Any attacker may read the source code and reverse-engineer the authentication mechanism to access parts of the application which would otherwise be protected.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-602
- PeerOf: CWE-300
- PeerOf: CWE-656

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential Mitigations
- [Architecture and Design] Do not rely on client side data. Always perform server side authentication.

## Demonstrative Examples (summary)
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
