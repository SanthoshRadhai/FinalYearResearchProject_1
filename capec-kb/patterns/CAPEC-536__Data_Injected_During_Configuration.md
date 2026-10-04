# CAPEC-536: Data Injected During Configuration

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/536.html  

## Description
An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to perform in a suboptimal manner that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- The attacker must have previously compromised the victim's systems or have physical access to the victim's systems.
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.

## Skills Required
- [High] Ability to generate and inject false data into operational data into a system with the intent of causing the victim to alter the configuration of the system.

## Mitigations
- Ensure that proper access control is implemented on all systems to prevent unauthorized access to system files and processes.

## Related Weaknesses (CWE)
- CWE-284
