# CWE-1390: Weak Authentication

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1390.html  

## Description
The product uses an authentication mechanism to restrict access to specific users or identities, but the mechanism does not sufficiently prove that the claimed identity is correct.

## Extended Description
Attackers may be able to bypass weak authentication faster and/or with less effort than expected.

## Related Weaknesses
- ChildOf: CWE-287

## Common Consequences
- Scope: Integrity, Confidentiality, Availability, Access Control; Impact: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands — This weakness can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with sensitive information or even execute arbitrary code.

## Demonstrative Examples (summary)
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
