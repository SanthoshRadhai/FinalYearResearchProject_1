# CAPEC-169: Footprinting

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/169.html  

## Description
An adversary engages in probing and exploration activities to identify constituents and properties of the target.

## Prerequisites
- An application must publicize identifiable information about the system or application through voluntary or involuntary means. Certain identification details of information systems are visible on communication networks (e.g., if an adversary uses a sniffer to inspect the traffic) due to their inherent structure and protocol standards. Any system or network that can be detected can be footprinted. However, some configuration choices may limit the useful information that can be collected during a footprinting attack.

## Skills Required
- [Low] The adversary knows how to send HTTP request, run the scan tool.

## Resources Required
- The adversary requires a variety of tools to collect information about the target. These include port/network scanners and tools to analyze responses from applications to determine version and configuration information. Footprinting a system adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Shut down unnecessary services/ports.
- Change default passwords by choosing strong passwords.
- Curtail unexpected input.
- Encrypt and password-protect sensitive data.
- Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.

## Related Weaknesses (CWE)
- CWE-200
