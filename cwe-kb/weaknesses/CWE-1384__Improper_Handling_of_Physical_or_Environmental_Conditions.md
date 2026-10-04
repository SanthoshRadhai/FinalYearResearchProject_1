# CWE-1384: Improper Handling of Physical or Environmental Conditions

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1384.html  

## Description
The product does not properly handle unexpected physical or environmental conditions that occur naturally or are artificially induced.

## Extended Description
Hardware products are typically only guaranteed to behave correctly within certain physical limits or environmental conditions. Such products cannot necessarily control the physical or external conditions to which they are subjected. However, the inability to handle such conditions can undermine a product's security. For example, an unexpected physical or environmental condition may cause the flipping of a bit that is used for an authentication decision. This unexpected condition could occur naturally or be induced artificially by an adversary. Physical or environmental conditions of concern are: Atmospheric characteristics: extreme temperature ranges, etc. Interference: electromagnetic interference (EMI), radio frequency interference (RFI), etc. Assorted light sources: white light, ultra-violet light (UV), lasers, infrared (IR), etc. Power variances: under-voltages, over-voltages, under-current, over-current, etc. Clock variances: glitching, overclocking, clock stretching, etc. Component aging and degradation Materials manipulation: focused ion beams (FIB), etc. Exposure to radiation: x-rays, cosmic radiation, etc.

## Related Weaknesses
- ChildOf: CWE-703

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Varies by Context, Unexpected State — Consequences of this weakness are highly dependent on the role of affected components within the larger product.

## Potential Mitigations
- [Requirements] In requirements, be specific about expectations for how the product will perform when it exceeds physical and environmental boundary conditions, e.g., by shutting down.
- [Architecture and Design, Implementation] Where possible, include independent components that can detect excess environmental conditions and have the capability to shut down the product.
- [Architecture and Design, Implementation] Where possible, use shielding or other materials that can increase the adversary's workload and reduce the likelihood of being able to successfully trigger a security-related failure.

## Demonstrative Examples (summary)
- Below is a representative snippet of C code that is part of the secure-boot flow. A signature of the runtime-firmware image is calculated and compared against a golden value. If the signatures match, the bootloader loads runtime firmware. If there is no match, an error halt occurs. If the underlying hardware executing this code does not contain any circuitry or sensors to detect voltage or clock glitches, an attacker might launch a fault-injection attack right when the signature check is happening (at the location marked with the comment), causing a bypass of the signature-checking process.
- In 2016, a security researcher, who was also a patient using a pacemaker, was on an airplane when a bit flip occurred in the pacemaker, likely due to the higher prevalence of cosmic radiation at such heights. The pacemaker was designed to account for bit flips and went into a default safe mode, which still forced the patient to go to a hospital to get it reset. The bit flip also inadvertently enabled the researcher to access the crash file, perform reverse engineering, and detect a hard-coded key. [REF-1101]
