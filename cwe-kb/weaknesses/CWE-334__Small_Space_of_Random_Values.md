# CWE-334: Small Space of Random Values

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/334.html  

## Description
The number of possible random values is smaller than needed by the product, making it more susceptible to brute force attacks.

## Related Weaknesses
- ChildOf: CWE-330

## Common Consequences
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — An attacker could easily guess the values used. This could lead to unauthorized access to a system if the seed is used for authentication and authorization.

## Potential Mitigations
- [Architecture and Design, Requirements] Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").

## Demonstrative Examples (summary)
- The following XML example code is a deployment descriptor for a Java web application deployed on a Sun Java Application Server. This deployment descriptor includes a session configuration property for configuring the session ID length.
