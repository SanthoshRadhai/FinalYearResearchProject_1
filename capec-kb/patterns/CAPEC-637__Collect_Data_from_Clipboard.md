# CAPEC-637: Collect Data from Clipboard

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/637.html  

## Description
The adversary exploits an application that allows for the copying of sensitive data or information by collecting information copied to the clipboard. Data copied to the clipboard can be accessed by other applications, such as malware built to exfiltrate or log clipboard contents on a periodic basis. In this way, the adversary aims to garner information to which they are unauthorized.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have a means (i.e., a pre-installed tool or background process) by which to collect data from the clipboard and store it. That is, when the target copies data to the clipboard (e.g., to paste into another application), the adversary needs some means of capturing that data in a third location.

## Skills Required
- [High] To deploy a hidden process or malware on the system to automatically collect clipboard data.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- While copying and pasting of data with the clipboard is a legitimate and practical function, certain situations and context may require the disabling of this feature. Just as certain applications disable screenshot capability, applications that handle highly sensitive information should consider disabling copy and paste functionality.
- Employ a robust identification and audit/blocking via using an allowlist of applications on your system. Malware may contain the functionality associated with this attack pattern.

## Related Weaknesses (CWE)
- CWE-267
