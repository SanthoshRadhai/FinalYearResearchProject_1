# CAPEC-624: Hardware Fault Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/624.html  

## Description
The adversary uses disruptive signals or events, or alters the physical environment a device operates in, to cause faulty behavior in electronic devices. This can include electromagnetic pulses, laser pulses, clock glitches, ambient temperature extremes, and more. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information.

## Prerequisites
- Physical access to the system
- The adversary must be cognizant of where fault injection vulnerabilities exist in the system in order to leverage them for exploitation.

## Skills Required
- [High] Adversaries require non-trivial technical skills to create and implement fault injection attacks. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required.

## Resources Required
- The relevant sensors and tools to detect and analyze fault/side-channel data from a system. A tool capable of injecting fault/side-channel data into a system or application.

## Consequences
- Scope: Confidentiality; Impact: Read Data, Bypass Protection Mechanism, Hide Activities
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Implement robust physical security countermeasures and monitoring.

## Related Weaknesses (CWE)
- CWE-1247
- CWE-1248
- CWE-1256
- CWE-1319
- CWE-1332
- CWE-1334
- CWE-1338
- CWE-1351
