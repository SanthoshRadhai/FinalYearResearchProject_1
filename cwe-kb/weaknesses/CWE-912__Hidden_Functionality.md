# CWE-912: Hidden Functionality

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/912.html  

## Description
The product contains functionality that is not documented, not part of the specification, and not accessible through an interface or command sequence that is obvious to the product's users or administrators.

## Extended Description
Hidden functionality can take many forms, such as intentionally malicious code, "Easter Eggs" that contain extraneous functionality such as games, developer-friendly shortcuts that reduce maintenance or support costs such as hard-coded accounts, etc. From a security perspective, even when the functionality is not intentionally malicious or damaging, it can increase the product's attack surface and expose additional weaknesses beyond what is already exposed by the intended functionality. Even if it is not easily accessible, the hidden functionality could be useful for attacks that modify the control flow of the application.

## Related Weaknesses
- ChildOf: CWE-684

## Common Consequences
- Scope: Other, Integrity; Impact: Varies by Context, Alter Execution Logic

## Potential Mitigations
- [Installation] Always verify the integrity of the product that is being installed.

## Detection Methods
- [Automated Static Analysis] Conduct a code coverage analysis using live testing, then closely inspect any code that is not covered.

## Demonstrative Examples (summary)
- In the example below, a malicous developer has injected code to send credit card numbers to the developer's own email address.
- Consider a device that comes with various security measures, such as secure boot. The secure-boot process performs firmware-integrity verification at boot time, and this code is stored in a separate SPI-flash device. However, this code contains undocumented "special access features" intended to be used only for performing failure analysis and intended to only be unlocked by the device designer.
