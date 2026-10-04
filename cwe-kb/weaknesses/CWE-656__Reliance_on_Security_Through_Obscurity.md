# CWE-656: Reliance on Security Through Obscurity

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/656.html  

## Description
The product uses a protection mechanism whose strength depends heavily on its obscurity, such that knowledge of its algorithms or key data is sufficient to defeat the mechanism.

## Extended Description
This reliance on "security through obscurity" can produce resultant weaknesses if an attacker is able to reverse engineer the inner workings of the mechanism. Note that obscurity can be one small part of defense in depth, since it can create more work for an attacker; however, it is a significant risk if used as the primary means of protection.

## Related Weaknesses
- ChildOf: CWE-657
- ChildOf: CWE-693
- CanPrecede: CWE-259
- CanPrecede: CWE-321
- CanPrecede: CWE-472

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Other; Impact: Other — The security mechanism can be bypassed easily.

## Potential Mitigations
- [Architecture and Design] Always consider whether knowledge of your code or design is sufficient to break it. Reverse engineering is a highly successful discipline, and financially feasible for motivated adversaries. Black-box techniques are established for binary analysis of executables that use obfuscation, runtime analysis of proprietary protocols, inferring file formats, and others.
- [Architecture and Design] When available, use publicly-vetted algorithms and procedures, as these are more likely to undergo more extensive security analysis and testing. This is especially the case with encryption and authentication.

## Demonstrative Examples (summary)
- The design of TCP relies on the secrecy of Initial Sequence Numbers (ISNs), as originally covered in CVE-1999-0077 [REF-542]. If ISNs can be guessed (due to predictability, CWE-330) or sniffed (due to lack of encryption during transmission, CWE-312), then an attacker can hijack or spoof connections. Many TCP implementations have had variations of this problem over the years, including CVE-2004-0641, CVE-2002-1463, CVE-2001-0751, CVE-2001-0328, CVE-2001-0288, CVE-2001-0163, CVE-2001-0162, CVE-2000-0916, and CVE-2000-0328.
