# CWE-1393: Use of Default Password

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1393.html  

## Description
The product uses default passwords for potentially critical functionality.

## Extended Description
It is common practice for products to be designed to use default passwords for authentication. The rationale is to simplify the manufacturing process or the system administrator's task of installation and deployment into an enterprise. However, if admins do not change the defaults, then it makes it easier for attackers to quickly bypass authentication across multiple organizations. There are many lists of default passwords and default-password scanning tools that are easily available from the World Wide Web.

## Related Weaknesses
- ChildOf: CWE-1392

## Common Consequences
- Scope: Authentication; Impact: Gain Privileges or Assume Identity

## Potential Mitigations
- [Requirements] Prohibit use of default, hard-coded, or other values that do not vary for each installation of the product - especially for separate organizations.
- [Documentation] Ensure that product documentation clearly emphasizes the presence of default passwords and provides steps for the administrator to change them.
- [Architecture and Design] Force the administrator to change the credential upon installation.
- [Installation, Operation] The product administrator could change the defaults upon installation or during operation.

## Demonstrative Examples (summary)
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
