# CAPEC-691: Spoof Open-Source Software Metadata

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/691.html  

## Description
An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and trusted.

## Related Attack Patterns
- ChildOf: CAPEC-690
- CanPrecede: CAPEC-184
- CanPrecede: CAPEC-444
- PeerOf: CAPEC-630

## Prerequisites
- Identification of a popular open-source component whose metadata is to be spoofed.

## Skills Required
- [Medium] Ability to spoof a variety of software metadata to convince victims the source is trusted.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Within package managers, look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related Weaknesses (CWE)
- CWE-494
