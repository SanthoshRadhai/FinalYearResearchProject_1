# CWE-784: Reliance on Cookies without Validation and Integrity Checking in a Security Decision

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/784.html  

## Description
The product uses a protection mechanism that relies on the existence or values of a cookie, but it does not properly ensure that the cookie is valid for the associated user.

## Extended Description
Attackers can easily modify cookies, within the browser or by implementing the client-side code outside of the browser. Attackers can bypass protection mechanisms such as authorization and authentication by modifying the cookie to contain an expected value.

## Related Weaknesses
- ChildOf: CWE-807
- ChildOf: CWE-565

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — It is dangerous to use cookies to set a user's privileges. The cookie can be manipulated to claim a high level of authorization, or to claim that successful authentication has occurred.

## Potential Mitigations
- [Architecture and Design] Avoid using cookie data for a security-related decision.
- [Implementation] Perform thorough input validation (i.e.: server side validation) on the cookie data if you're going to use it for a security related decision.
- [Architecture and Design] Add integrity checks to detect tampering.
- [Architecture and Design] Protect critical cookies from replay attacks, since cross-site scripting or other attacks may allow attackers to steal a strongly-encrypted cookie that also passes integrity checks. This mitigation applies to cookies that should only be valid during a single transaction or session. By enforcing timeouts, you may limit the scope of an attack. As part of your integrity check, use an unpredictable, server-side value that is not exposed to the client.

## Demonstrative Examples (summary)
- The following code excerpt reads a value from a browser cookie to determine the role of the user.
- The following code could be for a medical records application. It performs authentication by checking if a cookie has been set.
- In the following example, an authentication flag is read from a browser cookie, thus allowing for external control of user state data.
