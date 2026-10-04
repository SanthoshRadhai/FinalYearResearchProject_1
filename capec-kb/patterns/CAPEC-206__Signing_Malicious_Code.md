# CAPEC-206: Signing Malicious Code

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/206.html  

## Description
The adversary extracts credentials used for code signing from a production environment and then uses these credentials to sign malicious content with the developer's key. Many developers use signing keys to sign code or hashes of code. When users or applications verify the signatures are accurate they are led to believe that the code came from the owner of the signing key and that the code has not been modified since the signature was applied. If the adversary has extracted the signing credentials then they can use those credentials to sign their own code bundles. Users or tools that verify the signatures attached to the code will likely assume the code came from the legitimate developer and install or run the code, effectively allowing the adversary to execute arbitrary code on the victim's computer. This differs from CAPEC-673, because the adversary is performing the code signing.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The targeted developer must use a signing key to sign code bundles. (Note that not doing this is not a defense - it only means that the adversary does not need to steal the signing key before forging code bundles in the developer's name.)

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Ensure digital certificates are protected and inaccessible by unauthorized uses.
- If a digital certificate has been compromised it should be revoked and regenerated.
- Even if a piece of software has a valid and trusted digital signature, it should be assessed for any weaknesses and vulnerabilities.

## Related Weaknesses (CWE)
- CWE-732
