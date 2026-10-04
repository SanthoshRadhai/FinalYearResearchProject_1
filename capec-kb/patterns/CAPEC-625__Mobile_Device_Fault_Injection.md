# CAPEC-625: Mobile Device Fault Injection

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/625.html  

## Description
Fault injection attacks against mobile devices use disruptive signals or events (e.g. electromagnetic pulses, laser pulses, clock glitches, etc.) to cause faulty behavior. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information. Although this attack usually requires physical control of the mobile device, it is non-destructive, and the device can be used after the attack without any indication that secret keys were compromised.

## Related Attack Patterns
- ChildOf: CAPEC-624

## Skills Required
- [High] Adversaries require non-trivial technical skills to create and implement fault injection attacks on mobile devices. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required. This prerequisite makes the attack challenging to perform (assuming that physical security countermeasures and monitoring are in place).

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)
- Frequent changes to secret keys and certificates.

## Related Weaknesses (CWE)
- CWE-1247
- CWE-1248
- CWE-1256
- CWE-1319
- CWE-1332
- CWE-1334
- CWE-1338
- CWE-1351
