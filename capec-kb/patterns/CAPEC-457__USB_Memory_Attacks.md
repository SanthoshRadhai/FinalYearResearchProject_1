# CAPEC-457: USB Memory Attacks

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/457.html  

## Description
An adversary loads malicious code onto a USB memory stick in order to infect any system which the device is plugged in to. USB drives present a significant security risk for business and government agencies. Given the ability to integrate wireless functionality into a USB stick, it is possible to design malware that not only steals confidential data, but sniffs the network, or monitor keystrokes, and then exfiltrates the stolen data off-site via a Wireless connection. Also, viruses can be transmitted via the USB interface without the specific use of a memory stick. The attacks from USB devices are often of such sophistication that experts conclude they are not the work of single individuals, but suggest state sponsorship. These attacks can be performed by an adversary with direct access to a target system or can be executed via means such as USB Drop Attacks.

## Related Attack Patterns
- ChildOf: CAPEC-456
- CanPrecede: CAPEC-529

## Prerequisites
- Some level of physical access to the device being attacked.
- Information pertaining to the target organization on how to best execute a USB Drop Attack.

## Mitigations
- Ensure that proper, physical system access is regulated to prevent an adversary from physically connecting a malicious USB device themself.
- Use anti-virus and anti-malware tools which can prevent malware from executing if it finds its way onto a target system. Additionally, make sure these tools are regularly updated to contain up-to-date virus and malware signatures.
- Do not connect untrusted USB devices to systems connected on an organizational network. Additionally, use an isolated testing machine to validate untrusted devices and confirm malware does not exist.

## Related Weaknesses (CWE)
- CWE-1299
